N = int(input())
f = []
t = 0

for _ in range(N):
    s = int(input())
    if s % 10 != 0:
       f.append(s)
    t += s

if t % 10 == 0:
    if f:
        t -= min(f)
    else:
        t = 0
print(t)