N = int(input())
H = list(map(int, input().split()))

c = H[0]
for i in range(1,N):
    if c < H[i]:
        c = H[i]
        continue
    else:
        break
print(c)