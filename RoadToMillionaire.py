N = int(input())
A = list(map(int, input().split()))
m = 1000
a = A[0]
cnt = 0
i = 0
while i < N:
    if A[i] == a:
        i += 1
        continue
    elif A[i] > a:
        cnt = (m // a)
        m += (A[i] - a)*cnt
        a = A[i]
    elif A[i] < a:
        a = A[i]
    i += 1
print(m)
