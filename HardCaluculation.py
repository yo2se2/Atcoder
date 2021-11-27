A, B = input().split()

a = list(A)
b = list(B)

f = False
L = min(len(a),len(b))
for i in range(1,L+1):
    if (int(a[-i]) + int(b[-i])) // 10  != 0:
        f = True
        break

if f:
    print('Hard')
else:
    print('Easy')
