P = list(map(int, input().split()))
S = []

for p in P:
    S.append(chr(p+96))
print(''.join(S))