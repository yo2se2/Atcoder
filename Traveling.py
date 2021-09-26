N = int(input())
T = []
m = []
xy = [0,0]
f = True
pt = 0

for _ in range(N):
    t, x, y = map(int,input().split())
    T.append(t)
    m.append((x,y))

for i in range(N):
    t = abs(m[i][0]-xy[0]) + abs(m[i][1]-xy[1])
    # print(t,pt)
    if T[i] - t - pt >= 0:
        if (T[i] - t - pt) % 2 == 0:
            xy[0] = m[i][0]
            xy[1] = m[i][1]
            pt =T[i]
            continue
        else:
            f = False
            break
    else:
        f = False
        break

if f:
    print('Yes')
else:
    print('No')
