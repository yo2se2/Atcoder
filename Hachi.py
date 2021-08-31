from collections import Counter

S = input()
C = Counter(S)

if len(S) < 3:
    if int(S) % 8 == 0:
        print('Yes')
    else:
        print('No')
    exit()

for i in range(112,1000,8):
    f = True
    s = str(i)
    e = Counter(s)
    for j in e:
        if C[j] >= e[j]:
            continue
        elif C[j] < e[j]:
            f = False
            break
    if f:
        print('Yes')
        exit()
print('No')





