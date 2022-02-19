X = int(input())
x = list(str(X))
L = len(x)
f = False
if x[0] == '-':
    f = True
    x = x[1:]

l = x.pop()
# print(x,l)
if x:
    if f and l != '0':
        ans = (int(''.join(x)) + 1)
        if f:
            print(-ans)
        else:
            print(ans)
    else:
        ans = (int(''.join(x)))
        if f:
            print(-ans)
        else:
            print(ans)

else:
    if f:
        print(-1)
    else:
        print(0)