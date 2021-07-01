N = int(input())
cnt = 0
L = []
for a in range(2,int(N**0.5)+1):
    b = 2
    while N >= a**b:

        L.append(a**b)
        b += 1

print(N-len(set(L)))
