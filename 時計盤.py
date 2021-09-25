n, m = map(int, input().split())

n = n % 12


L = 30 * n + (m*0.5)
S = 6 * m

print(min(abs(L-S),360-abs(L-S)))