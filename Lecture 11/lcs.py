def lcs(s,t):
    T = [[0 for i in range(len(t))] for j in range(len(s))]
    maxLen = 0

    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                if i > 0 and j > 0:
                    T[i][j] = T[i-1][j-1] + 1
                else:
                    T[i][j] = 1
                maxLen = max(maxLen,T[i][j])
    return maxLen