from collections import Counter

N = int(input())
A = list(map(int, input().split()))

C = Counter(A)

for num in C:
    if C[num] != 4:
        ans = num
print(ans)