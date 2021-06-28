X, K, D = map(int,input().split())

c = (abs(X) // D) + 1

if K <= c:
    if X < 0:
        X = X + K*D
    elif X > 0:
        X = X - K*D
    elif X == 0:
        if (K % 2) != 0:
            X = X + D


else:
    if X < 0:
        if (K - c) % 2 == 0:
            X =  X + c*D
        else:
            X = X + c*D -D
    elif X > 0:
        if (K - c) % 2 == 0:
            X = (X - c*D)
        else:
            X = X - c*D + D
    elif X == 0:
        if (K % 2) != 0:
            X = X + D
print(abs(X))