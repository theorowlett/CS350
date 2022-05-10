## Lecture 10 - Dynamic Programming
---
### Algorithimic Strategies
- When working on algorithms problems we usually employ algorithmic strategies.
- We did this with divide and conquer
  - Divide and conquer works by dividing and conquering
  - I kid, but not really
- Divide and conquer has a big drawback
  - Some pieces might overlap
  - This affects the running time, makes it mo' bad.
---
### Fibonacci numbers
- f_0 = 0
- f_1 = 1
- f_2 = 0 + 1 = 1
- f_3 = 1 + 1 = 2
- f_3 = 1 + 2 = 3
- ...
```python
def fib(n):
    if n <= 1:
        return n
    else
    return fib(n-1) + fib(n-2)
```
- This looks good, it's bad though.
- Let's find a more efficient version
---
### Dynamic Programming
- Top down: memoization
  - A top down algorithim is where we solve the problem by breaking it into smaller problems
  - Recursion
- bottom up: build tables
  - We solve the simplest version of the problem, then build up the solution over time.
  - Loop
  - No stack overflow (you can still look it up there though hehehehehe_lizard.gif)
---
### Top Down - Memoization
- Made up word, came from making a memo.
- Look at fib.py for example
- The trick:
  - If it exists, then we return the value
  - if it doesn't, then we compute it and store the value.
  - We call this finding the optimal substructure
- **This is important af**
  - Ever call that is memoized runs in $O(1)$
  - Every call that isn't memoized makes 2 recursive calls
  - Every call that isn't memoized runs in $O(n)$ time (for + and i)
  - Every number is called at least once.
  - $$ \sum_{i=1}^n i + 2O(1) = \theta(n^2)$$
  - We had a discussion in class that blew up my brain just now. Rebooting Theo.

---
### Binomial Coefficients
- If i have $(x+y)^n$, then I can use binomial theorem to FOIL.
```python
def choose(h,k):
if k==0 or k==h:
    return 1
return choose(h,k-1) + choose(h-1,k)
```
- This is bad.
- Look at binomial.py for a mo' betta version.

---
### The Knapsack Problem

- Given a list of items where each item is a pair (v,w) where v is the value of the item and w is the weight, and a bag with capacity C, what is the value of the subset of items that will fit in the bag with the largest value?
  - Diamonds cost $1000, weigh 7 lbs
  - Rubies $500, 4lbs
  - Saphires $300, 3 lbs
  - Sack can only hold 20lbs
- For each item (v_i, w_i) we either include it or we don't