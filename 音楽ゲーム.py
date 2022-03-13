N = int(input())
X = []

for _ in range(N):
    x = list(input())
    X.append(x)
ans = 0
for i in range(N):
    for j in range(9):
        if X[i][j] == '.':
            continue
        elif X[i][j] == 'x':
            ans += 1
        elif X[i][j] == 'o':
            ans += 1
            c = i
            while c < N and X[c][j] == 'o':
                X[c][j] = '.'
                c += 1
print(ans)