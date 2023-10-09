N, M  = map(int, input().split())
L = list(map(int, input().split()))

t = 0

maxW = sum(L) + N-1

l = 0
r = maxW

def f(w: int):
    line = 0
    rem = 0
    for i in range(N):
        if rem >= L[i]+1:
            rem -= L[i]+1
        else:
            line += 1
            rem = w-L[i]
        if rem < 0:
            return False

    if line <= M:
        return True
    else:
        return False
cnt = 0
while r-l > 1:
    m = (r+l)//2
    cnt += 1
    if f(m):
        r = m
    else:
        l = m
    # print("{}回目 l:{}, r:{}".format(cnt,l,r))

if f(l):
    print(l)
else:
    print(r)
