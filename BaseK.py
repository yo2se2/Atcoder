K = int(input())
A, B = map(int,input().split())

def base_n_to_10(X,n):
    out = 0
    for i in range(1, len(str(X)) + 1):
        out += int(X[-i]) * (n ** (i - 1))
    return out

ans = base_n_to_10(str(A),K) * base_n_to_10(str(B),K)

print(ans)