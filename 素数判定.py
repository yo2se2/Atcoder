N = int(input())

x = int(N ** 0.5)
f = True

# 素数判定
for i in range(2, x + 1):
    if N % i == 0:
        f = False
        break

n = str(N)

ad = 0

for s in n:
    ad += int(s)

if N == 1:
    ans = 'Not Prime'
elif f:
    ans = 'Prime'
elif ad % 3 != 0 and int(n[-1]) % 2 != 0 and int(n[-1]) != 5:
    ans = 'Prime'
else:
    ans = 'Not Prime'
print('{}'.format(ans))
