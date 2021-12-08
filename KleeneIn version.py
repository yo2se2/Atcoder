N, K = map(int, input().split())
A = list(map(int, input().split()))

mod = 10**9+ 7

front = 0
back = 0
for i in range(N):
    for j in range(i+1,N):
        if A[i] < A[j]:
            back += 1
        if A[i] > A[j]:
            front += 1

ans = 0
ans = (front*K*(K+1)) + (back*K*(K-1))
ans = int(ans//2)

print(ans%mod)




