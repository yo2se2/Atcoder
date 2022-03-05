N = int(input())
A = list(map(int, input().split()))
a = []
t = 0
c = 0
f = False

for i in range(N):
    t += abs(A[i])
    a.append(abs(A[i]))
    if A[i] < 0:
        c += 1
    elif A[i] == 0:
        f = True
if c % 2 == 0:
    ans = t
elif c % 2 == 1:
    if f:
        ans = t
    else:
        ans = t - 2 * min(a)
print(ans)