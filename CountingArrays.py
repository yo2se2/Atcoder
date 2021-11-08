N = int(input())
A = set()
for _ in range(N):
    a = list(map(str, input().split()))
    s = ' '.join(a)
    A.add(s)
L = len(A)
print(L)
