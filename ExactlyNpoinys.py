N = int(input())

cs = 0
ans = []
c = 1
while cs <= N:
    cs += c
    ans.append(c)
    c += 1
d = cs-N
for a in ans:
    if a != d:
        print(a)





