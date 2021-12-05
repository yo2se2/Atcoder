N = int(input())
r = list(input())
ans = 0

for g in r:
    if g == 'A':
        ans += 4
    elif g == 'B':
        ans += 3
    elif g == 'C':
        ans += 2
    elif g == 'D':
        ans += 1
ans /= N
print("{}\n".format(ans))
