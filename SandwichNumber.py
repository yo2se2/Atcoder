S = list(input())
f = False
if len(S) == 8:
    f = True
    for i in range(8):
        if i == 0:
            if  'A' <= S[i] and S[i] <= 'Z':
                continue
            else:
                f = False
                break
        elif i == 7:
            if 'A' <= S[i] and S[i] <= 'Z':
                continue
            else:
                f = False
                break
        elif i == 1:
            if '1' <= S[i] and S[i] <= '9':
                    continue
            else:
                f = False
                break
        else:
            if '0' <= S[i] and S[i] <= '9':
                continue
            else:
                f = False
                break


if f:
    print('Yes')
else:
    print('No')
