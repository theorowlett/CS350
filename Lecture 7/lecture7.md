## Lecture 7 - Recurrance
---
$$ \sum_{i=1}^n ia^i = \frac {a-(n+1)a^{n+1} +na^{n+2}} {(i-a)^2}$$
- I don't need to remember this but here it is
---
### Constant Time
- A closed form of a recursive function is a function that computes the same valuse, but doesn't have recursion.
- They're good bc:
  - Constant time
  - Easy to understand
  - No stack overflow
- Factorial Recursively:
  - $$ n! = n*(n-1)! $$
- Fibonacci numbers:
  - $$a_1 = 1$$
  - $$a_2 = 1$$
  - $$ a_n = a_{n-1} + a_{n-2} $$
---
### Solving Recurrances
- Guessing is an option
  - This can be hard
  - Sometimes it's not
  - It's worth a shot
- Harder example
$$ a_0 = 1 $$
$$ a_n = 2 * a_{n-1} + n$$
- Substitution method
  - Unroll the recursion. (There's a lot here that I'm not going to transcribe, look at page 7 of the slides)
  - Drawbacks
    - It's hard
    - It's not always apparent
  - Fibonnaci (again)
    - $$ f_n = f_{n-1} + f_{n-2} $$
    - Once again we're going too fast, look at the the slides on page 12.
    - Basically it's a circle. Can't do it without figuring it out.
- Divide and Conquer Recurrances
  - Let's look at a merge sort:
```python
def mergeSort(lst):
  if len(lst) <= 1:
    return lst
  n2 = len(lst)//2
    return merge(mergeSort(lst[:n2]),mergeSort(lst[n2:]))
```
  - Every divide and conquer looks like this:
    - $T(n) =aT(\frac n b) + f(n)$
    - We did more substitution method
---
### Recursion and Theta Notation
- Two assumptions
  - we are working with divide and conquer
  - we don't care about exact answer
# The Master Theorem (This is where the fun begins)
- Suppose $T(n) = aT(\frac n b) + f(n)$
- Then
  - if $f(n) < \theta(n^{log_b(a)}) $ then ...
  - Finish copything this down later
- Give $\theta$
  - T(1) = 1
  - $T(n) = T(\frac n 2) +1$
    - a = 1
    - b = 2
    - f(n) = 1
    - $$ \theta(n^{\log_2(1)}) $$
    - $$ \theta(\log_2(n))
  - T(1) = 1
  - $T(n) = T(\frac n 2) +n$