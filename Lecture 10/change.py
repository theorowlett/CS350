# target amount t
# Make change with the fewest coins possible
# WE MAKE A NEW COIN
# Screwup == 7 cents

def change(coins,cap):
    memos = [None] * (cap+1)
    return change_memo(coins,cap,memos)

def change_memo(coins,t,memos):
    if memos[t] is not None:
        return memos[t]
    minCoins = t
    for val in coins:
        count = 0
        if t >= val:
            count = change_memo(coins, t-val, memos) + 1
    minCoins = min(minCoins,count)
    memos[t] = minCoins
    return minCoins