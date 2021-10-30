from math import ceil

N, M = map(int, input().split())
B = []
for _ in range(N):
    b = list(map(int, input().split()))
    B.append(b)

ans = 'Yes'

for i in range(N):
    if i > 0:
        if B[i][0] != B[i-1][0] + 7:
            ans = 'No'
            break
    if ceil(B[i][0]/7) != ceil(B[i][M-1]/7):
        ans = 'No'
        break
    for j in range(1,M):
        if B[i][j] != B[i][j-1] + 1:
            ans = 'No'
            break

print(ans)
