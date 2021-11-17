x1, y1, r = map(int, input().split())
x2, y2, x3, y3 = map(int, input().split())
rf = False
bf = False

def distance(x,y,a,b):
    return ((x-a)**2 + (y-b)**2)**0.5

squere = [(x2,y2),(x2,y3),(x3,y2),(x3,y3)]

if x2 <= x1 and x1 <= x3 and y2 <= y1 and y1 <= y3:
    if x1 + r > x3:
        rf = True
    else:
        bf = True
    if x1 - r < x2:
        rf = True
    else:
        bf = True
    if y1 + r > y3:
        rf = True
    else:
        bf = True
    if y1 - r < y2:
        rf = True
    else:
        bf = True
    for p in squere:
        if distance(x1, y1, p[0], p[1]) > r:
            bf = True
        elif distance(x1, y1, p[0], p[1]) < r:
            rf = True
else:
    for p in squere:
            if distance(x1,y1,p[0],p[1]) > r:
                rf = True
                bf = True
            elif distance(x1,y1,p[0],p[1]) < r:
                rf = True
if rf:
    print('YES')
else:
    print('NO')

if bf:
    print('YES')
else:
    print('NO')

