c =[input().split() for _ in range(4)]

for i in range(2):
    for j in range(4):
        c[i][j], c[3-i][3-j] = c[3-i][3-j], c[i][j]
for i in c:
    print(' '.join(i))



