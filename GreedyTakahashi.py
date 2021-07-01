A, B, K = map(int, input().split())

def eat_cookie(a: int,b: int, k: int):
    if a >= k:
        a -= k
    else:
        b = b - (k - a)
        a = 0
        if b < 0:
            b = 0
    return a,b

a , b = eat_cookie(A,B,K)

print(a,b)