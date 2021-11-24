N, K = map(int, input().split())
P = []
S = []
for i in range(N):
    p = list(map(int,input().split()))
    P.append(p)
    s = (i, sum(p))
    S.append(s)

newS = sorted(S, key=lambda x: x[1], reverse=True)
base = newS[K-1][1]

for i in range(N):
    if S[i][1] + 300 >= base:
        print('Yes')
    else:
        print('No')

