# items = [(1000,7),(500,4),(300,3)]
# cap = 20

# This is the first example in class
# runtime is bad.
def recursive_knapsack(items,cap):
    maxVal = 0
    for (val,weight) in items:
        if cap >= weight:
            val = recursive_knapsack(items, cap-weight) + val
            maxVal = max(maxVal,val)
    return maxVal


def knapsack(items,cap):
    memos = [None] * (cap+1)
    return knapsack_memo(items,cap,memos)

def knapsack_memo(items,cap,memos):
    if memos[cap] is not None:
        return memos[cap]
    maxVal = 0
    for (val,weight) in items:
        if cap >= weight:
            val = recursive_knapsack(items, cap-weight, memos) + val
        maxVal = max(maxVal,val)
        memos[cap] = maxVal
    return maxVal

    
