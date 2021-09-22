N = int(input())
A = list(map(int, input().split()))
c = [0]
for i in range(N):
    c.append(c[i]+ A[i])
total = c[-1]

Min = 10**10
for i in range(1,N):
    X = c[i]
    Y = total - X
    ans = abs(X-Y)
    if ans < Min:
        Min = ans
print(Min)
