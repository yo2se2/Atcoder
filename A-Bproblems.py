A, B = input().split()

lA = list(A)
lB = list(B)

for i,a in enumerate(lA):
    if a != '9':
        lA[i] = '9'
        break
for i,b in enumerate(lB):
    if i == 0:
        if b != '1':
            lB[i] = '1'
            break
    else:
        if b != '0':
            lB[i] = '0'
            break

ans = max(int(A)-int(''.join(lB)),int(''.join(lA))-int(B))
print(ans)
