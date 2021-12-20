H, W = map(int, input().split())
C = [['#' for _ in range(W+2)]]
l = [[0 for _ in range(W+2)] for _ in range(H+2)]

for _ in range(H):
    c = list(input())
    C.append(['#'] + c + ['#'])
C.append(['#' for _ in range(W+2)])

for i in range(H,-1,-1):
    for j in range(W,-1,-1):
        if C[i][j] == '#':
            continue
        else:
            l[i][j] = max(l[i+1][j],l[i][j+1]) + 1

print(l[1][1])