S = list(input().split())
N = int(input())
T = []
L = []
for s in S:
    L.append(len(s))


for i in range(N):
    t = input()
    T.append(t)

for t in T:
    l = len(t)
    for j in range(len(S)):
        if L[j] == l:
            f = True
            for k in range(l):
                if t[k] == '*' or t[k] == S[j][k]:
                    continue
                else:
                    f = False
                    break
            if f:
                S[j] = '*'*l
print(' '.join(S))




