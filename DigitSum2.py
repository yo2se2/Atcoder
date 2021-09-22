N = input()
n = list(N)

A = str(int(N) + 1)
ans = 9 * (len(list(A))-1)

ans += int((list(A)[0])) - 1

print(ans)