## Lecture 2 - Math Review and Computational Complexity
---
### Convex Hull Problem
-  For a set of points, the convex hull is all of the points on the outside.
-  Given a list of points which are pairs of (x,y) coordinates, find the list of points in the convex hull.
   -  if two points p1 and p2 form a line on the convex hull, then every other...
   -  p1 = (x1,y1)
   -  p2 = (x2,y2)
   -  Standard form of a line: ax + by = c
   -  Find a,b,c
      -  a = y2 -y1
      -  b = x2 -x1
      -  c = x1y2 -x2y1
   -  if ax + by > c then p on the left hand side of the line.
   -  reverse for right side

---
### Exponents and Logs
- Exponent Theorems
  - $$ a^0 = 1 $$
  - $$ a^1 = a $$
  - $$ a^{b+c} = a^ba^c $$
- Log Therorems
  - For all rational numbers a and b 
    - $$ a^{loga(b)} = b $$
    - $$ log(a^b) = b $$
  - We'll always be using log<sub>2</sub> for this class. ==Because Binary Trees==

---

### Summation Theroems
- $\sum_{i=m}^{\infty} n^2$ this is just example syntax.
- ==Get these from the slides later, too fast for in class==.

---

### Matrices

- a vector *v* is a sequence of numbers
- *n* is the dimension of the vector
- Dot Product
  - $\sum_{i=1}^{n} ui*vi$

---

### Analyzing Algorithims

- Timing isn't always the best definition.
  - Data set size can change what algorithim is more efficient for a given use case.
- A program scales with funtion f: N -> R^+ if, for input of size n it takes f(n) times to run.
- If we're running on a faster computer, te program might run in half the time
- This makes measures algorithims exactly problematic.
-  ==Page 33 of the slides for the definition==
-  