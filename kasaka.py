S = list(input())
L = len(S)
f = True
l = 0
r = L-1
c = 0
for i in range(L-1,L//2-1,-1):
    if S[i] == 'a':
        c += 1
    else:
        break


while l < r:
    if S[l] == S[r]:
        l += 1
        r -= 1
    else:
        if l < c and S[r] == 'a':
            r -= 1
        else:
            f = False
            break
if f:
    print('Yes')
else:
    print('No')
