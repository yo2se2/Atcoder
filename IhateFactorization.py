X = int(input())

for a in range(-1000,1000):
    for b in range(-1000,1000):
        x = a**5 - b**5
        if X != x:
            continue
        elif X == x:
            print(a, b)
            exit()
print(0,-1)