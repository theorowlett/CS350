from heapq import heappush, heappop

# O((V+E)log(E))

def prim(g):
    mst = []
    q = []
    # (w,u,v) 
    # -- w -weight of edge
    # -- u - vertex already visited
    # -- v - vertex going to
    heappush(q, (0,0,0))
    seen = set()
    while len(q) != 0:
        # Were w,p,u now because reasons
        # same order as w,u,v
        (w,p,u) = heappop(q)
        if u not in seen:
            seen.add(u)
            if p!= u:
                mst.append((p,u))
            for (v,w) in g[u]:
                if v not in seen:
                    heappush(q, (w,u,v)) 
    return  mst