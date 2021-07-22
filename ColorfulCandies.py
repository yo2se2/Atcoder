#   尺取り法
N, K = map(int,input().split())
C = list(map(int,input().split()))

dic = {}
for i in C[:K]:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
kinds = len(dic)

Max = kinds
for j in range(N-K):
    dic[C[j]] -= 1
    if dic[C[j]] == 0:
        kinds -= 1

    if C[j+K] in dic:
        dic[C[j+K]] += 1
    else:
        dic[C[j+K]] = 1

    if dic[C[j+K]] == 1:
        kinds += 1

    if Max < kinds:
        Max = kinds

print(Max)