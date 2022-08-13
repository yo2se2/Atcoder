import math

a, b, x = map(int, input().split())

if x <= (a*a*b)/2:
    ans = math.degrees(math.atan((b * b * a)/(2*x)))
else:
    ans = math.degrees(math.atan(2*((a*a*b)-x)/(a**3)))

print(ans)