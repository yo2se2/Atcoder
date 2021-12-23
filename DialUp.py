N, M = map(int, input().split())
S = list(map(int,input().split()))
T = list(map(int,input().split()))
ans = 0
trans = 0

if set(T) <= set(S):
    f = False
    for i in range(1,N//2+1):
        if S[i] == S[0] and S[-i] == S[0]:
            continue
        elif S[i] != S[0]:
            trans = i
            break
        elif S[-i] != S[0]:
            trans = i
            break

    for t in T:
        if t == S[0]:
            ans += 1
        elif t != S[0]:
            if f == False:
                S[0] = t
                ans += trans + 1
                f = True
            else:
                ans += 2
                S[0] = t
    print(ans)

else:
    print(-1)


