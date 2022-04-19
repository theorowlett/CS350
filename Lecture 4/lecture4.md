## Lecture 4 - Non Linear Structures (and some Linear contd.)
---
### Queues
- Using a Vector
  - Ring buffer is the best approach.
  - Instead of always starting from the front, we keep track of two indices front and back.
  - Having the pointers wrap around works, but then resizing can be weird.
  - Within Python we have to manually resize, cannot use `append()` when we reach the size of the vector.
---
### Dequeues
- Pronounced **deck**
- Basically just a ring buffer queue with push and pop from both sides.
---
### Sets
- Sets: $x \in S$
- Maps: $M[k] \in v$
  - Python objects are just maps.
  - Keanu_whoa.gif
- Priority Queues: return minimum element.
- Sets require:
  - add(x)
  - lookup(x)
- There are more operations like union and intersection, but add and lookup are required.
- In Python, we use the in operator for lookup.
```python
class ListSet():
  def __init__(self):
    self.body = []

  def add(self, x):
    self.body.append(x)
    
  def lookup(self, x):
    return x in self.body
```
- add(x) $O(1)$ amortized
- lookup(x) $O(n)$
  - We can do better with lookup.
- What about binary search?
  - Would cause lookup(x) in $O(\log(n))$
  - But add(x) would be $O(n)$
---
### Trees
- So we have two good options:
  - Trees
    - A tree is either a Leaf(x)
    - or it's a Branch(x,t<sub>1</sub>,t<sub>2</sub>...t<sub>n</sub>)
    - where t<sub>1</sub>,T<sub>2</sub>...t<sub>n</sub> are tree
```python
class Leaf():
  def __init__(self, value):
    self.value = value
class Branch():
  def __init__(self, value, ts):
    self.value = value
    self.children = ts
  def child(self, i):
    return self.children[i]
```

```python
class Branch():
    def __init__(self,)
```
  - **Theo, get better at trees**
  - Theorem: a complete binary tree of height *n* has size %2^n -1$
    - Base case: The size of Leaf(x) is 1.
    - indutive hypothesis: If I and r are complete binary trees of height k, then they have size $2^k -1$
    - INductive case:
      - The height of 5 = Node(x,l,r) is k+1
      - The size of t is 1 plus the size of I pus the size of r.
      - By the inductive hypothesis the size of I and r is $2^k -1$.
      - So the size of *t* is:
        - $$1 + (2^k -1) + (2^k -1) $$
        - **Finish taking notes on the proof, page 14 of slides**
      - If the BST is unbalanced, you can have $O(n)$ time to lookup.
      - With balanced tree:
        - If a tree has size *n*, then it has height $\log_2 (n)$
        - Means our lookup time is $\theta(\log(n))$
      - But we have to balance the tree
        - Red black:
          1. All paths must have the same number of black nodes.
          2. You can't have two red nodes in a row.
          - In any red black tree, the length of the longest path is no more then twice the length of the shortest path.
          -   
  - Hash Sets

---
### Hash Sets
- Sometimes definitely maybe better than a balanced tree.
- Use an array as a set, but mo' betta
  - Create a set of numbers {1,3,7,9,11}
```python
s = [False] * 12
s[3] = s[5] = s[7] = s[9] = s[11] = True
```
  - This works really well for efficiency, but it takes a ton of memory.
  - How can we make it better?
    - Fixed size array
```python
class HashSet():
    def __init__(self):
        self.body = [False] * 1000
      def add(self,x):
          self.body[x % 1000] = True
```
  - But this will have collisions :(
  - How can we deal with collisions?
    - Bucket chaining: list of lists
    - open addressing (probing): flat list, find next free spot