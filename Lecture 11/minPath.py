def minPath(dag,u,v):
    def topSort(i,v):
        seen[i] = True
        sorted = [i]
        if i == v:
            return sorted
        for j in range(len(dag[i])):
            if seen[dag[i][j]] == False:
                sorted += topSort(dag[i][j],v) 
        return sorted

    n = len(dag)
    # d is the weight table
    d = [float('inf') for i in range(n)]
    d[u] = 0
    seen = [False for i in range(n)]

    # dag is tuples since it's weighted
    # It's in the notes somethere?
    for s in topSort(u,v):
        for (t,w) in dag[s]:
            if d[t] > d[s] + w:
                d[t] = d[s] + w
    return d[v]

