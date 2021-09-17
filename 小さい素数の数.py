n = int(input())

def eratones(x):
    if x == 0 or x == 1:
        return 0
    else:
        is_prime = [True for _ in range(x)]
        is_prime[0] = False
        is_prime[1] = False
        i = 2

        while i <= (x**0.5):
            if is_prime[i]:
                f = i*i
                for j in range(i*i,x,i):
                    is_prime[j] = False
            i += 1
        return is_prime.count(True)

print(eratones(n))