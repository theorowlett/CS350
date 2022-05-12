def warshall(adj):
    T = adj
    for w in range(len(adj)):
        for u in range(len(adj)):
            for v in range(len(adj)):
                if T[u][w] == 1 and T[w][v] == 1:
                    T[u][v] = 1

    return T