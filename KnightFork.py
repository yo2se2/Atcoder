x1, y1, x2, y2 = map(int, input().split())

d = ((1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2))
L1 = []
L2 = []
for dx, dy in d:
    L1.append((x1+dx,y1+dy))
    L2.append((x2+dx,y2+dy))
f = False
for L in L1:
    if L in L2:
        f = True
        break

if f:
    print('Yes')
else:
    print('No')