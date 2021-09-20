N, Q = map(int, input().split())
S = input()
c = [0 for _ in range(N+1)]
for i in range(N):
    if S[i:i+2] == 'AC':
        c[i+1] = c[i] + 1
    else:
        c[i+1] = c[i]

for _ in range(Q):
    l, r = map(int, input().split())
    print(c[r-1]-c[l-1])
