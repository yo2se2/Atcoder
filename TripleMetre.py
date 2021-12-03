S = input()
L = len(S)
f = True
i = 0

s = 'oxx' * 10

List_s = [s[:L],s[1:L+1],s[2:L+2]]


if S in List_s:
    print('Yes')
else:
    print('No')

