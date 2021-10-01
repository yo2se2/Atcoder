N = int(input())
S = list(input())
Q = int(input())
f = False

for _ in range(Q):
    T, A, B = map(int, input().split())
    if T == 1:
        if f:
            if A > N:
                A = A - N
            else:
                A = A + N
            if B > N:
                B = B - N
            else:
                B = B + N

        S[A-1],S[B-1] = S[B-1],S[A-1]

    elif T == 2:
        f = not(f)

if f:
    ans = S[N:] + S[:N]
else:
    ans = S

print(''.join(ans))
