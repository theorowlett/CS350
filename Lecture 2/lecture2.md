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
  - $$ a^{b-c} = a^b / a^c $$
  - $$ a^{bc} = (a^b)^c
- Log Therorems
  - For all rational numbers a and b 
    - $$ a^{loga(b)} = b $$
    - $$ log(a^b) = b $$
  - Properties of logs
    - For all rational numbers a and b, and c:
    - ==Fill these in later==
  - We'll always be using log<sub>2</sub> for this class. ==Because Binary Trees==

---

### Summation Theroems
- A summation is:
  - $$\sum_{i=m}^{n} a_i = a_m + a_{m+1} + ... a_n $$
- Example:
  - $$\sum_{i=1}^n i = 1 + 2 + 3 + ... n $$ 
- Theorem: index addition:
  - $$\sum_{i=m}^{n-1} a_i + \sum_{i=n}^c a_i = \sum_{i=m}^c a_i $$
- Index Swap:
  - $$\sum_{i=m}^{n} a_i = \sum_{i=n}^{m} a_i $$
- Constant Multiplication:
  - $$\sum_{i=m}^{n} c * a_i = c * \sum_{i=m}^{n} a_i $$
- Commutativity:
  - $$\sum_{i=m}^{n} a_i + b_i = \sum_{i=m}^{n} a_i + \sum_{i=m}^n b_i $$
- Index offset:
  - $$\sum_{i=m}^{n} a_i = \sum_{i=m+p}^{n+p} a_{i-p} $$
- Summation Swap:
  - $$\sum_{i=m}^{n} \sum_{j=c}^d a_{i,j} = \sum_{j=c}^{d} \sum_{i=m}^n a_{i,j} $$
- Log Product
  - $$\sum_{i=m}^n \log(a_i) = \log(\prod_{i=m}^n a_i) $$
- Special series
  - Constant series
    - $$\sum_{i=1}^n c = c*n $$
  - Linear Series
    - $$\sum_{i=1}^n i = \frac {n(n+1)} 2 $$
  - Geometric Series
    - $$\sum_{i=0}^n a* r^i = \frac {a(r^{n+1} - 1)} {r-1} $$
  - Telescoping Series
    - $$\sum_{i=1}^n x_i -x_{i+1} = x_1 -x_n $$

---

### Matrices

- a vector *v* is a sequence of numbers
- *n* is the dimension of the vector
- Dot Product
  - $$ \sum_{i=1}^{n} ui*vi $$

---

### Analyzing Algorithims

- Timing isn't always the best definition.
  - Data set size can change what algorithim is more efficient for a given use case.
- A program scales with funtion f: N -> R^+ if, for input of size n it takes f(n) times to run.
- If we're running on a faster computer, te program might run in half the time
- This makes measures algorithims exactly problematic.
-  ==Page 33 of the slides for the definition==
-  