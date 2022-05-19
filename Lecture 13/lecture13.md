## Lecture 13 - More greedy algorithims
---
### The minimum spanning tree problem
- Given a weight graph G, what is the subgraph T where
  - T is a tree
  - if u in V(G), then u in V(T)
  - $$\sum_{(u,v)} in T^{} $$
---
### Prim's algorithim
- start with a single vertex (it does not matter)
- at each step we add the vertex closest to the current tree
- we stop when we've reached the full tree
- How do we knw what edge to pick next?
  - Lowest weight edge, but how?
  - A heap!
  - heappush and heappop from heapq are super useful.
- How do we know if adding an edge will add a cycle?
  - Remember what vertices we've seen.
- how do this actually return?
  - It returns a Tree, but it's easier to return a list of edges in the tree. We can reconstruct the tree later.
---
### Kruskals algorithim
- Sort the edges
- Keep taking edges from the sorted list
- skip any edges that would form a cycle
- Keep track of what vertices belong to what trees:
  - put each vertex into a set
  - When joining two tree, we union their sets
