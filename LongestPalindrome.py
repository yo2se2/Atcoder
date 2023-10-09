S = input()

def pal(l,r,str):
    s = l
    e = r
    while l < r:
        if str[l] == str[r]:
            r -= 1
            l += 1
        else:
            return -1
    return e-s + 1
ans = -1

for l in range(len(S)):
    for r in range(len(S)-1,-1,-1):

        ans = max(ans,pal(l,r,S))

print(ans)