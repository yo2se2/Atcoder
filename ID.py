N, M = map(int, input().split())

d = {}

for i in range(M):
    p, y = map(int, input().split())
    if p in d:
        d[p].append((y,i))
    else:
        d[p] = [(y,i)]


id = [0 for _ in range(M)]

for P in d:
    d[P].sort(key=lambda x: x[0])
    for i in range(len(d[P])):
        idx = d[P][i][1]
        id[idx] =  str(P).zfill(6) + str(i+1).zfill(6)
for ID in id:
    print(ID)