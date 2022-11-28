A, B = map(int, input().split())

g = ((2*B)/A)**(-2/3)
if int(g) != 0:
    ans = min(B * (int(g)-1) + (A/(int(g)**0.5)),B * (int(g)) + (A/((int(g)+1)**0.5)))
else:
    ans = B * (int(g)) + (A/((int(g)+1)**0.5))
print(ans)
