# qs[r] = c
def queens(n):
    return _queens_rec([],n)

def _queens_rec(qs,n):
    if len(qs) == n:
        print(qs)
    
    row = len(qs)
    for c in range(n):
        if c not in qs and all_safe(qs,row,c):
            _queens_rec(qs+[c],n)

def all_safe(qs,r,c):
    for old_r in range(len(qs)):
        old_c = qs[old_r]
        dr = abs(r-old_r)
        dc = abs(r-old_c)
        if dr == dc:
            return False
    return True
    
queens(3)



