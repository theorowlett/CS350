## Lecture 8 - Graphs
---
### Graphs
- Formally a graph G is a tuple (V,E) of vertices and edges.
- $$ E \subset V * V $$
- V = {a,b,c,d,e}
- E = {(a,b),(a,c),(b,c)(b,d),(d,e),(c,e)}
- Different ways to represent graphs
  - implict
    - Don't represent the graph
    - Most common with state space graph
    - Ex: $2*\log_2(x)+\log_2(5)$
    - $2\log_2(5x)$
    - $5x$
    - This is a graph! (I believe)
  - expicit
    - Created in memory. Vectors are nodes, edges are pointers to other node/vectors.
  - edge list
    - really simple, space efficiency
    - easy to extend/append
    - searching is $O(n)$
    - don't know what the vertices are w/o traversing
  - adjancency list
    - We gonna use this **a lot**
    - use a dictionary/hashmap, store all vertices connected to a vertex
    - Looking up is constant time
    - Connecting nodes is quick
    - Somewhat space efficient
    - Looking up edges is O(n)
  - adjacency matrix
    - You make a matrix of 1's and 0's
    - Undirected graphs are always symmetric
---

## Efficiency Discussion
- instead of input being measured as n, we need to look at V, E
---

## Classifying Graphs
- Cycle - a graph where all of the nodes conect in a ring
- Complete graph - every node is connected to every other graph
  - A complete graph is a cycle but not every cycle is a complete graph
- hypercube - outline of an n-dimensional cube.
- Empty graph - no edges
- Bipartate graphs - iff it's vertices can be divided into 2 sets.
  - Must be given 2 different sets
  - To determine if a graph is bipartite:
    - Pick a vertex, make it S
    - All adjacent vertices are in T
    - Those adjacent vertices are in S
    - if all vertices accounted for, it is bipartite.
- Petersen Graph - It sucks, super weird.
- If you have a graph where v1 ~ v2 it means the vertices are connected
- Theorem time
> for a graph G, $2 * |E| = \sum_{v \set{V}} deg(V)$
- |E| represents tje number of edges connected