from collections import Counter

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a = Counter(A)
b = Counter(B)
ans = 0
ans2 = 0

for i in range(N):
    if A[i] == B[i]:
        ans += 1
        a[A[i]] -= 1
        b[B[i]] -= 1
    elif b[A[i]]:
        ans2 += 1
print(ans)
print(ans2)
