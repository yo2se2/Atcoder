N = int(input())
A = list(map(int, input().split()))


x = 0
s = 0
for a in A:
    s += abs(a - x)
    x = a
s += abs(A[-1])
A = [0] + A + [0]

for i in range(1,N+1):
    ans = s - abs((A[i] - A[i-1])) - abs(A[i+1]-A[i]) + abs(A[i+1]-A[i-1])
    print(ans)
