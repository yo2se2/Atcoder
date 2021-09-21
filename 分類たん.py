s = input()
S = list(s)
f = False

for i in range(len(S)):
    if S[i] == ' ':
        if f:
            S[i] = ''
        elif not(f):
            f = True
            S[i] = ','

    else:
        f = False

print(''.join(S))