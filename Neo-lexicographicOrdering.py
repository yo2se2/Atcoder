X = input()
dic = {}
c = 1
for i in list(X):
    dic[i] = c
    c += 1

N = int(input())
S = []
sc = []
for _ in range(N):
    s = input()
    score = [0 for _ in range(10)]
    for i,v in enumerate(s):
        score[i] = (dic[v])
    sc.append([s,tuple(score)])

sc.sort(key = lambda x:(x[1][0],x[1][1],x[1][2],x[1][3],x[1][4],x[1][5],x[1][6],x[1][7],x[1][8],x[1][9]))


for i in sc:

    print(i[0])