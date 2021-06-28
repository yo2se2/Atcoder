N = int(input())
A = list(map(int,input().split()))
mod = 10**9 + 7
total = sum(A)
answer = 0
t = 0

for i in range(N):
    t += A[i]
    answer += (total-t)*A[i]

print(answer%mod)