N = int(input())

def make_divisor(x):
    lower_divisor = []
    higher_divisor = []
    i = 1
    while (i * i) <= x:
        if x % i == 0:
            lower_divisor.append(i)

            if (x // i) != i:
                higher_divisor.append(x//i)
        i += 1

    return lower_divisor + higher_divisor[::-1]

answer = make_divisor(N)

for i in answer:
    print(i)