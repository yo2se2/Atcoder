S = input()
T = input()
f = False
for k in range(27):
    a = []
    for s in S:
        ns = ((ord(s) + k) - ord('a')) % 26
        ns += ord('a')
        a.append(chr(ns))
    ans = ''.join(a)
    if ans == T:
        f = True
        break
if f:
    print('Yes')
else:
    print('No')