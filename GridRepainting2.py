H, W = map(int, input().split())
S = [['.' for _ in range(W+2)]]
for _ in range(H):
    s = list(input())
    S.append(['.'] + s + ['.'])
S.append(['.' for _ in range(W+2)])

def check(x,y,S):
    d = [(x+1,y),(x-1,y),(x,y-1),(x,y+1)]
    f = False
    for nx, ny in d:
        if S[ny][nx] == '.':
            continue
        elif S[ny][nx] == '#':
            f = True
    return f

for i in range(1,H+1):
    for j in range(1,W+1):
        if S[i][j] == '.':
            continue
        elif S[i][j] == '#':
            if check(j,i,S):
                continue
            else:
                print('No')
                exit()
print('Yes')
