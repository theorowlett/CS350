# Traveling Slesman
# Given an unweighted graph, give the tour with the minimum
# weight.

def salesman(g):
    return salesman_rec([0],g,0)

def salesman_rec(path,g,w):
    if len(g) == len(path):
        return (path, w+g[path[-1]][0])

    minPath = list(range(len(g)))
    minWeight = 0
    for v in range(len(g)):
        minWeight += g[v][(v+1)%len(g)]
    for v in range(len(g)):
        if v not in path:
            (newPath, newWeight) = salesman_rec(path+[v],g,w+g[path[-1][v]])
            if newWeight < minWeight:
                minPath = newPath
                minWeight = newWeight
    return (minPath,minWeight)   

def main():
    adj_list = [
        [0,1,4,8,6],
        [1,0,7,11,2],
        [4,7,0,9,12],
        [8,11,9,0,3],
        [6,2,12,3,0]
    ]
    print(salesman(adj_list))

if __name__ == '__main__':
    main()

    
