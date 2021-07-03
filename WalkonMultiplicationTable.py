# 約数列挙

N = int(input())

def sum_divisor(n):
    A = []
    i = 1
    answer = 0
    min = 10 << 63
    while i < int(n**0.5)+1:
        if n % i == 0:
            if n // i > i:
                answer = (i-1) + ((n // i)-1)
            else:
                answer = (i-1) + (i-1)

        if answer < min:
            min = answer
        i += 1

    return min

print(sum_divisor(N))