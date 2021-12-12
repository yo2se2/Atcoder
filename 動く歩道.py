L, X, Y, S, D = map(int, input().split())

if D >= S:
    r = D - S
    l = (L-D) + S
else:
    r = (L-S)+D
    l = S - D
lt = 10**9
rt = r / (X + Y)
if Y-X > 0:
    lt = abs(l / (Y-X))
if S == D:
    lt = 0
print(min(lt,rt))