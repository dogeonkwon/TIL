p = 'REA'
t = 'WHEREAREYOU'
M = len(p)
N = len(t)

def BruteForce(p,t):
    i = 0
    j = 0
    while j < M and i < N:
        if t[i] != p[j]:
            i = i-j
            j = -1

        i = i+1
        j = j+1
    if j == M:
        return i, M, i-M
    else:
        return -1

print(BruteForce(p,t))