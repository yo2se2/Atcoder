#尺取り法
from math import factorial
N = int(input())
A = list(map(int, input().split()))
ans = 0
l  = 0

def comb(n,r):
    return factorial(n)//factorial(n-r)//factorial(r)
ans = N

while l < N:
    r = l+1

    while r < N and A[r-1] < A[r]:
        r += 1
    if r-l > 1:
        ans += comb(r-l,2)
    l = r
print(ans)