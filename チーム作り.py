from math import ceil

n = int(input())
L = ceil(n/20)

if L % 2 == 0:
    f = True
else:
    f = False

if f:
    ans = ((n-(L*20))*-1)+1
else:
    ans = n-((L-1)*20)

print(ans)