from math import gcd

def lcm(a,b):
    return (a * b) // gcd(a, b)

N = int(input())
A = list(map(int, input().split()))
B = A.copy()
L = len(A)

while L > 1:
    a = B.pop()
    b = B.pop()
    B.append(lcm(a,b))
    L -= 1

Y = B.pop() - 1
ans = 0
for X in A:
    ans += Y % X

print(ans)