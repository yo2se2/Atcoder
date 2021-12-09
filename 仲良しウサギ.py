N = int(input())
v = [False for _ in range(N+1)]
v[0] = True
ans = 0
A = list(map(int, input().split()))

for i in range(N):
    if not(v[i+1]):
        v[i+1] = True
        if A[A[i]-1] == i+1:
            ans += 1
            v[A[i]] =True
print(ans)