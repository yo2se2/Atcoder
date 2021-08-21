N = int(input())

i = 0
ans = 0

while 2**i <= N:
    ans = i
    i += 1
print(ans)