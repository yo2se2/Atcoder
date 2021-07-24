S = []
for _ in range(4):
    s = input()
    S.append(s)

if len(set(S)) == 4:
    print('Yes')
else:
    print('No')



