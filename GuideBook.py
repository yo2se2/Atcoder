N = int(input())
S = []
P = []

for i in range(N):
    s, p = input().split()
    S.append((i+1,s))
    P.append((i+1,int(p)))


sortS = S.sort(key=lambda x: x[1])
ans = []

i = 0
l = S[i][1]

score = list()
while i < N:
    if l == S[i][1]:
        score.append(P[S[i][0]-1])
        i += 1

    elif l != S[i][1]:
        score.sort(key=lambda x: x[1], reverse=True)
        ans += score
        score.clear()
        l = S[i][1]

score.sort(key=lambda x: x[1], reverse=True)
ans += score

for a in ans:
    print(a[0])




