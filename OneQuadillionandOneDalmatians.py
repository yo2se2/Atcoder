N = int(input())

d = []

while N > 0:
    s = ord('a')

    if N == 0:
        break
    else:
        N -= 1
        c = N % 26
    N //= 26
    d.append(chr(s+c))
ans = ''
for c in reversed(d):
    ans += c
print(ans)

