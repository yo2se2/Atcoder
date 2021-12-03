from math import ceil
N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
d = []
m = 10 **  9

for i in range(M):
    diff = False
    if i == 0:
        if A[i] == 1:
            continue
        else:
            diff = A[i]-1

    elif i == M-1:

        if A[i] != N:
            d.append(A[i]-A[i-1]-1)
            d.append(N - A[i])
        else:
            diff = (N - A[i-1]-1)
    else:
        diff = A[i]-A[i-1]-1

    if diff:
        d.append(diff)
if d:
    m = min(d)

# print(d,m)
ans = 0
for i in d:
    ans += ceil(i/m)
if M == 0:
    ans = 1
print(ans)