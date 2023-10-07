N, M, P = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

B.sort()
b_prefix = [0]*(M+1)
for i in range(M):
    b_prefix[i+1] = b_prefix[i] + B[i]

def BinarySearch(L: list, s: int):

    l = 0
    h = len(L)

    while l < h:
        m = (h + l) // 2
        if L[m] <= s:
            l = m + 1
        else:
            h = m
    return l
ans = 0

for a in A:
    s = P-a
    idx = BinarySearch(B,s)

    ans += idx*a
    ans += (M-idx)*P
    ans += b_prefix[idx]

print(ans)



