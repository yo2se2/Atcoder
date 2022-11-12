N = int(input())
str1 = ['H', 'D', 'C', 'S']
str2 = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
d = {}
f = True

for _ in range(N):
    s = input()

    if not(s[0] in str1):
        f = False

    if not(s[1] in str2):
        f  = False

    if s in d:
        f = False
    else:
        d[s] = True

if f:
    print('Yes')
else:
    print('No')


