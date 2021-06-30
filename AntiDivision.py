import math
A, B, C, D = map(int, input().split())

def my_lcm(x, y):
    return (x*y) // math.gcd(x,y)

n = B - A + 1

E = my_lcm(C,D)

a  = (B // C) - ((A-1) // C)
b  = (B // D) - ((A-1) // D)
c  = (B // E) - ((A-1) // E)


answer = n - a - b + c
print(answer)
