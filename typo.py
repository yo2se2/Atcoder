S = list(input())
T = list(input())
L = len(S)
f = True
c = 0

for i in range(L-1):
    if S[i] == T[i]:
        continue
    else:
        if S[i+1] == T[i] and S[i] == T[i+1]:
            S[i], S[i+1] = S[i+1], S[i]
            break
        else:
            print('No')
            exit()
for i in range(L):
    if S[i] == T[i]:
        continue
    else:
        f = False

if f:
    print('Yes')
else:
    print('No')

