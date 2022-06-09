## Final Exam Review
---
### Not quite Sloth
- Using union without path compresssion or union by rank, what is the results of the following operations. {1},{2},{3},{4},{5}
>union(2,3)
>union(1,3)
>union(4,5)
>union(4,1)
>        4
>    2       5
>1       3    

---
### One Step Forward (Backtracking probs)
- Suppose youre dropped in the middle of a random maze, does the "follow the left wall" algorithim still work? Why or why not?
  - No, because you could be caught in a cyclical loop.
  - It works if you're not starting in the middle because you're starting with an outer wall
---
### Graphic Content (Graphs)
- If a DA has V vertices, what is the largest number of edges it could have?
  - $\frac {v^2-v} 2$
- Give a topological ordering of the following DAG.
  - Get the actual graph from someone else
  - DFS. If 'A' comes before 'B' in the topological ordering B cannot have an edge to A.
  - x,t,q,u,w,v,y,r,m , then reverse 
  - m,r,y,v,w,u,q,t,x
---
### Try {} Catch Me if you can 
- 100: Give an algorithim to determine if a directed graph is a DAG.
  - BFS, we give each number a number based upon distance from origin. If a larger node connects to a smaller node, we have a cycle.
- 200: I want to add memoization to the following algo. Why won't it speed up the algo?
  - Because we never recalculate the numbers
- 300: What is the Huffman Tree for "it was the best of times, it was the blurst of times? you stupid monkey!"
  - Count the number of times characters occur, then sort them

---
### Napolean Dynamite
- 100: 
