# 文字列全探索
S = input()
T = input()
Ls = len(S)
Lt = len(T)

cnt = 0
Min = 10**4

for i in range(Ls-Lt+1):
    s = i
    diff = 0
    for j in range(Lt):
        if S[s] != T[j]:
            diff += 1
        s += 1
    if diff < Min:
        Min = diff
print(Min)
