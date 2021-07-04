from collections import Counter

w = input()
W = list(w)

c = Counter(W)

for i in c:
    if c[i] % 2 != 0:
        print('No')
        exit()

print('Yes')

