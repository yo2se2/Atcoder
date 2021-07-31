X = input()
x = list(map(int,X))
flag1 = False
flag2 = False
for i in range(3):
    if x[i+1] == x[i] + 1:
        continue
    elif x[i+1] == 0 and x[i] == 9:
        continue
    else:
        flag1 = True
        break
for i in range(3):
    if x[i+1] == x[i]:
        continue
    else:
        flag2 = True
        break


if flag1 and flag2:
    print('Strong')
else:
    print('Weak')

