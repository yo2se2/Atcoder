N, M = map(int, input().split())

c = {}

for i in range(N+1):
    c[i] = i

play = 0
for _ in range(M):
    d = int(input())
    stop = play
    play = d
    c[play],c[stop] = 0,c[d]

c2 = sorted(c.items(), key = lambda x:x[1])

for x,y in c2:
    if y == 0:
        continue
    else:
        print(x)
