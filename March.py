from itertools import combinations

per = combinations(list('MARCH'), 3)

N = int(input())
name = {}

for i in list('MARCH'):
    name[i] = 0

for _ in range(N):
    s = input()
    if (s[0] in 'MARCH'):
        if s[0] in name:
            name[s[0]] += 1
ans = 0
for i in per:
    ans += name[i[0]] * name[i[1]] * name[i[2]]
print(ans)
