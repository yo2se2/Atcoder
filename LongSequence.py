N = int(input())
A = list(map(int,input().split()))
X = int(input())

Asum = [0]
for i in range(N):
    Asum.append(Asum[i] +  A[i])

ans = (X//Asum[-1]) * N
B = X % Asum[-1]
i = 0

while B >= 0:
    B = B - A[i]
    ans += 1
    i += 1

print(ans)



