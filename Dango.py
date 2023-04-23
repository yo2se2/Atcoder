N = int(input())
S = list(input())


def Level(L):
    n = len(S)
    ans = -1
    l, r = 0, 0
    while r < n:
        if l == r:
            r += 1
        if L[l] == '-':
            cnt = 0
            while r < n and L[r] == 'o':
                cnt += 1
                r += 1
            l = r
            if cnt != 0:
                ans = max(ans,cnt)
        else:
            l += 1
    return ans

print(max(Level(S),Level(S[::-1])))
