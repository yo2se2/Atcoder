N = int(input())
v = [False for _ in range(N+1)]
T = []
K = []
A = []
for _ in range(N):
    s = list(map(int, input().split()))
    T.append(s[0])
    K.append(s[1])
    A.append(s[2:])

ans = T[N-1]
for n in A[N-1]:
    stack = []
    if not(v[n]):
        v[n] = True
        stack.append(n)
    while stack:
        nt = stack.pop()
        ans += T[nt-1]
        for a in A[nt-1]:
            if not(v[a]):
                v[a] = True
                stack.append(a)
print(ans)





