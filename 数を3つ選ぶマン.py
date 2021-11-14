A, B, C, D, E = map(int, input().split())
L = [A,B,C,D,E]
S = set()
for i in range(3):
    for j in range(i+1,4):
        for k in range(j+1,5):
            # print(i,j,k)
            S.add(L[i]+L[j]+L[k])
S = list(S)
S.sort()
print(S[-3])
