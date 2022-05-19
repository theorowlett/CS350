def kruskal(g):
    # (w,u,v) 
    # -- w -weight of edge
    # -- u - vertex already visited
    # -- v - vertex going to
    edges = sorted([(w,u,v) for u in range(len(g)) for (v,w) in g[u]])
    sets = [{v} for v in range(len(g))]
    # for every v, v in s[v]
    s = list(range(len(g)))

    mst = []

    for (w,u,v) in edges:
        if u not in set[s[v]]:
            sets[s[u]] |= sets[s[v]]
            for x in sets[s[v]]:
                s[x] = s[u]
            mst.append((u,v))
    return mst