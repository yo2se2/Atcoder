N, A, B = map(int, input().split())
S = []
t = 0

for _ in range(N):
    s = int(input())
    t += s

    S.append(s)
m = min(S)
M = max(S)
if M-m == 0:
    print(-1)
    exit()
else:
    ave = t/N
    P = B/(M-m)
    Q = A - P*ave
    print(P,Q)



