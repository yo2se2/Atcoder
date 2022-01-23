N, M = map(int, input().split())
S = list(input().split())
T = list(input().split())

d = {}

for s in S:
    d[s] = False

for t in T:
    d[t] = True

for s in S:
    if d[s]:
        print('Yes')
    else:
        print('No')
