def slow_choose(h,k):
    if k==0 or k==h:
        return 1
    return slow_choose(h,k-1) + slow_choose(h-1,k)

def choose(n,k):
    memos = [[None] * k + 1 for i in range(n+1)]
    return choose_rec(n,k,memos)

def choose_rec(n,k,memos):
    if memos[n][k] is not None:
        return memos[n][k]
    if k == 0 or k == n:
        memos[n][k] = 1
        return 1
    val = choose_rec(n-1,k,memos) + \
        choose_rec(n-1,k-1,memos)
    memos[n][k] = val
    return val