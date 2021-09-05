S = input()
T = input()
c = 'atcoder'
f = True

for i in range(len(S)):
    if S[i] == T[i]:
        continue
    elif S[i] == '@':
        if T[i] in c:
            continue
        else:
            f = False
            break
    elif T[i] == '@':
        if S[i] in c:
            continue
        else:
            f = False
            break
    else:
        f = False
        break
if f:
    print('You can win')
else:
    print('You will lose')
