# 全探索　最大公倍数の問題
import math
K = int(input())
answer = 0

for a in range(1,K+1):
    for b in range(1,K+1):
        ab = math.gcd(a,b)
        for c in range(1, K+1):
            # print("a= {},b ={},c = {}の最大公約数は{}".format(a,b,c,math.gcd(c,ab)))
            answer += math.gcd(c,ab)
print(answer)