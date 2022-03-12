N = int(input())
d = {}
for i in range(N):
    x, y = map(int, input().split())
    if y in d:
        d[y].append((x,i))
    else:
        d[y] = [(x,i)]

S = input()

ans = 'No'

for i in d:
    d[i].sort(key = lambda x:x[0])
    f = True
    for x, i in d[i]:
        if f:
            if S[i] == 'R':
                f = False
        else:
            if S[i] == 'L':
                ans = 'Yes'
                print(ans)
                exit()
print('No')



