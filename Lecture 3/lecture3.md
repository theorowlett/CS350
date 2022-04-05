## Lecture 3 - Linear Structures
---
### Random Early Class Discussion
- We can assume that multiplication is $n^2$ time.
- Bit shift is constant time.
- Assume incrementation is $O(n)$

---
### Data Structures
- *Abstract Data Type* tells us what an object can do.
- *Data structures* tells us how the object does it.
- ADT is the interface, a data structure is the implementation.

---
### Python Object Model
```python
class Pokemon(): #  this is a class for pokemon
  def __init__(self, type, number): #Constructor
    self.type = type
    self.dexno = number
  #Method, in C++ this is a member function, here it's a method.
  def generation(self): 
    if dexno <= 151:
      return 1
```
- `__init__` is constructor
  - self has to be first argument every time.
  - `self.fieldname` inside constructor is *HIGHLY* recommended.
    - Python can and will make new variables whereever it wants.
- `__str__` is how to print, readable
- Python *kind of* has inheritance
```python
def Charmander(Pokemon):
    def __init__(self):
        super().__init__(fire,4)
```
- Since Python is dynamically typed, we can inherit implementation, not interface
  - This is inheritance of implementation
  - C++ is inheritance of interface
  - This means that if I write a method in the Pokemon class, I can call if from Charmander.
---
### ADT Example: Sequences
- Sequence:
  - Create(size)
  - lookup(i)
  - append(x)
- Arrays are the simplest type of Sequence.
  - $O(n)$ creation time
  - $O(1)$ lookup time
    - Great up until now.
  - $\theta(n^2)$ append time
    - That's bad.
  - They have a major of disadvantage of not being resizable.
```python
class Array():
  def __init__(self, size):
    self.body = [0] * size
  def lookup(self, i):
    return self.body[i]
  def append(self, x):
    newBody = [0] * (len(self.body)+1)
    for i in range(len(self.body)):
      newBody[i] = self.body[i]
      newBody[len(self.body)] = x
      self.body = newBody
```
- So what can we do better?
- Linked Lists are *garbage* but we have to talk about them.
  - Linked lists are worse because arrays are contiguous in memory, linked lists definitely are not.
    - It's hard to cacche when memory is all over the place. Cache miss rate is through the heckin roof.
    - Making linked lists in Python is painful so I'm not going to transcribe those notes. __DEALWITHIT.GIF__
  - Efficiencies:
    - Create(n): $\theta(n)$
    - Lookup(i): $\theta(i)$
    - Append(x): $\theta(x)$
  - What do linked lists do well:
    - Insert into the middle of a list
    - Guarantee that the of the time the nodes in a link list never move in memory.
    - These situations don't really come up in algorithims.
- Vectors: Vectors are lists in Python
  - It's pretty much an array that can grow quickly.
  - Amortized Anaysis: The average time analysis, rather than best or worst case.
    - Example: Inrememnting a binary number.
      - Algorithim:
      1. Go to last bit,
      2. Look at the current bit,
      3. If it's 0 flip it to 1 and exit.
      4. If it's 1 flip it to 0.
      5. Go to Step 2.
    - Worst case $O(n)$, best case is $O(1)$
    - Half te time, the last digit will be 0.
    - 1/4 of the time the second to last digit will be 0.
    - 1/8th of the time the third to last digit will be 0.
    - $$\sum_{i=1}^\log(n) \frac {in} {2^i} = O(n)$$
    - So count runs in amortized time: $O(i)$
    - Efficiency
      - Create(n) : $\theta(n)$
      - Lookup(i) : $\theta(1)$
      - Append(x) : $\theta(1)$ ammortized