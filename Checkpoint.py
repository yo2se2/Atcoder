N, M = map(int, input().split())
students = []
check = []
for _ in range(N):
    a, b = map(int, input().split())
    students.append((a,b))

for _ in range(M):
    c, d = map(int,input().split())
    check.append((c,d))

for i in range(N):
    Min = 10**9
    ans = -1
    x1 = students[i][0]
    y1 = students[i][1]
    for j in range(M):
        x2 = check[j][0]
        y2 = check[j][1]
        L = abs(x1-x2) + abs(y1-y2)
        if L < Min:
            Min = L
            ans = j + 1
    print(ans)