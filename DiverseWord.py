S = input()
F = [True for _ in range(26)]

L = len(S)

if L < 26:
    for c in S:
        F[ord(c)-ord('a')] = False
    for i,f in enumerate(F):
        if f:
            print(S+chr(ord('a')+i))
            break
else:
    # 後ろから見ていって、既に見た文字が、発見した文字より後ろであればそれで置き換えて出力
    found = []
    for i in range(len(S) - 1, -1, -1):
        for f in found:
            if S[i] < f:
                print(S[:i] + f)
                exit(0)
        found.append(S[i])
        found.sort()
    else:
        print(-1)


