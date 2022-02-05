N = int(input())
A = list(map(int, input().split()))

o = [0]
d = 0
for a in A:
    d = (d + a) % 360
    o.append(d)
ans = 0

o.sort()
o.append(360)

for i in range(1,len(o)):
    diff = o[i]-o[i-1]

    if ans < diff:
        ans = diff
print(ans)
