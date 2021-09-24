X, Y = map(int, input().split())

p = [X]
while X*2 <= Y:
    p.append(X*2)
    X  *= 2

print(len(p))