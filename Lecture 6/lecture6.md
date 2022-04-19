## Lecture 6 - Divide and Conquer
---
### Midterm stuff
- Next Thursday
- On paper
- One sheet of notes allowed, no calculator/computers
- Maybe about 10 quesitons, we'll go over it next Tuesday

---
### Divide and Conquer (Recursion)
- Binary Search Algorithim
  - If the list is empty, x isn't in it
  - compare x to the middle
  - if x == middle, we done
  - If x > ,search upper half
  - If x < , search lower half
  - repeat
- This problem works really well with recursion
- **Challenge**
  -  Write a binary search where you only compile your code once. (This is python, so by compile we mean running code)
  -  No looking up stuff on the internet.
  -  If you can do this, you're a champ.
- Binary Search example:
```python
Binary Search
def binSearch(lst, l, h, x):
  m = (l+h)//2
  if lst[m] == x:
    return True
  if l >= h:
    return False
  if lst[m] > x:
    return binSearch(lst, l, m, x)
  else:
    return binSearch(lst, m, h, x)
```
- **Recurrance Relation**: is a recursive function $T: \mathbb{N} -> N$
  - In the above binSearch, each recursive call will do 3 comparisons
  - Each pass can only make one recursive call
  - Each recursive call will have a length of n/2 relative to parent call.
  - So the recursive relation is:
    - $$ T(1) = 1 $$
    - $$ T(n) = T(\frac n 2) + \theta(1) $$
    - Or we could say to be exact:
    - $$ T(n) = T(\frac n 2) + 3 $$
---
### Merge Sort
- simplest outside of heapsort
- Sorting a deck of cards:
  - split into two piles
  - sort the piles
  - merge the piles together
```python
# I wrote this. If it's busted don't hate me.
# l1 = [1,3,5]
# l2 = [2,4,6]
def merge(l1,l2):
    sorted = []
    i = j = 0
    while i < len(l1) or j < len(l2):
        if l1[i] < l2[j]:
            sorted.append(l1[i])
            i += 1
        else:
            sorted.append[l2[j]]
            j+= 1
    if i < len(l1):
        sorted += l1[i:]
    elif j < len(l2):
        sorted += l2[j:]
    return sorted 
```
- This was what we decided in class:
```python
# l1 = [1,3,5]
# l2 = [2,4,6]
def merge(l1,l2):
    sorted = []
    i = j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            sorted.append(l1[i])
            i += 1
        else:
            sorted.append[l2[j]]
            j+= 1
    # This last line is too clever for it's own good.
    # It's too dangerous to be left alive, we must kill it Jim.
    return sorted + l1[i:] + l2[j:]
```
- input size `n = len(l1) + len(l2)`
- Since at least one counter is incrementing (i or j), runtime is $\theta(n)$
- Now we're going to use merge to write mergesort:
```python
def mergesort(l):
    if len(l) <= 1:
        return l
    n = len(l)//2
    return merge(mergesort(l[n:]),mergesort(l[:n]))
```
- T(1) = 1
- T(n) = 2T (finish this later)
---  
### Quick sort
- We pick a pivot
- Everything < pivot is small
- Everything > pivot is big
- Then we sort small and big
- Example:
  - `[5,3,8,7,2,9,4]`
  - pivot = 4, small = [3,2,4], big = [8,7,9]
    - sort small
    - pivot = 3, small, 2, big 3
    - return [2,3,4]
- 3 things to consider:
  - How much time does it take to split?
    - n
  - How many recursive calls?
    - 2
  - How big are the sublists?
    - `n//2`
  - T(1) = 1
  - T(n) = T(n-1) + 1 + n
  - That's $n^2$...
- If we feed quicksort an already sorted list, It's $n^2$
- Same thing with reverse sorted.
- Some ways to mitigate: 
  - pick 3 pivots (start,mid,end)
  - pick a random pivot
  - 
