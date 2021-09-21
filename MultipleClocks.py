from  math import gcd
N = int(input())
T = []
for _ in range(N):
    t  = int(input())
    T.append(t)
def lcm(x,y):
    return (x*y) // gcd(x,y)
A = T[0]
for i in range(1,N):
    nA = lcm(A,T[i])
    A = nA
print(A)