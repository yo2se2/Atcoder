N = int(input())
A = list(map(int, input().split()))

def check_rate(x: int):
    if 1 <= x and x <= 399:
        ans = 'Gray'
    elif 400 <= x and x <= 799:
        ans = 'Brown'
    elif 800 <= x and x <= 1199:
        ans = 'Green'
    elif 1200 <= x and x <= 1599:
        ans = 'sky'
    elif 1600 <= x and x <= 1999:
        ans = 'Blue'
    elif 2000 <= x and x <= 2399:
        ans = 'Yellow'
    elif 2400 <= x and x <= 2799:
        ans = 'Orange'
    elif 2800 <= x and x <= 3199:
        ans = 'Red'
    else:
        ans = False
    return ans

s = set()
c = 0
for a in A:
    r = check_rate(a)
    if r:
        s.add(r)
    else:
        c += 1
if len(s) == 0 and c > 0:
    print(1, c)
else:
    print(len(s), len(s)+c)