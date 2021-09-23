N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = []
S = 0
a = 0
for i in range(N):
    if B[i] > A[i]:
        a += 1
        S += B[i] - A[i]
    else:
        C.append(A[i]-B[i])

C.sort()
num = 0
ans = 0
while S > num:
    if C:
        num += C.pop()
        ans += 1
    else:
        print(-1)
        exit()
print(ans+a)
