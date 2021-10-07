S = list(input())

c = list('keyence')
l = len(c)
L = len(S)
newS = []
j = 0

for i in range(len(S)):
    if j < l:
        if S[i] == c[j]:
            newS.append(S[i])
            j += 1
        else:
            newS = newS + S[L-(l-j):]
            break
    else:
        newS = []
        break

if newS == c:
    print('YES')
else:
    print('NO')