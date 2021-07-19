N = int(input())
m = []
for i in range(N):
    x, y = map(int,input().split())
    s = (x,y)
    m.append(s)


c = 1
ans = 0
for i in m:
    x1 = i[0]
    y1 = i[1]
    for j in range(c,len(m)):
        x2 = m[j][0]
        y2 = m[j][1]
        # print(x1,y1,x2,y2)
        a = (y2-y1)/(x2-x1)

        if -1 <= a and a <= 1:
            ans += 1
    c += 1
print(ans)

