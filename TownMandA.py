N = int(input())
S = []
P = []
total = 0
for _ in range(N):
    s, p = input().split()
    S.append(s)
    P.append(int(p))
    total += int(p)

h = total / 2
for i in range(N):
    if P[i] > h:
        print(S[i])
        exit()

print('atcoder')