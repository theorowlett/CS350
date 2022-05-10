def main():
    petersen = [
        [1,4,5],    #0
        [0,2,6],    #1
        [1,3,7],    #2
        [2,4,8],    #3
        [0,3,9],    #4
        [0,7,8],    #5
        [1,8,9],    #6
        [2,5,9],    #7
        [3,5,6],    #8
        [4,6,7],    #9
    ]

def maxDeg(g):
    _largest = float('-inf')
    n = len(g)
    for i in range(n):
        sum = 0
        for j in range(len(n[i])):
            if g[i][j] == 1:
                sum += 1
        _largest = max(sum,_largest)
    return _largest

def size(g):
    degs = 0
    for v in g:
        degs += len(v)
    return degs//2


main()