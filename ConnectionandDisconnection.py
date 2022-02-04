S = input()
K = int(input())
L = len(S)

c = S[0]
cnt = 1

C = []
for i in range(1,L):
    if S[i] == c:
        cnt += 1
    else:
        C.append(cnt)
        c = S[i]
        cnt = 1
C.append(cnt)
ans = 0
if len(C) > 1 and S[0] == S[-1]:
    ans += ((C[0]+C[-1])//2)*(K-1)
    for i in range(1,len(C)-1):
        ans += (C[i]//2)*K
    ans += C[0]//2
    ans += C[-1]//2
elif len(C) == 1:
    ans = (L*K) //2
else:
    for i in range(len(C)):
        ans += (C[i]//2)*K
print(ans)