N, M = map(int, input().split())

class UnionFind():

    def __init__(self,n):
        self.n = n
        # 親ノードのインデックス・ノード数を表す
        self.par = [-1 for _ in range((self.n)+1)]

    # xとyを結合させる。　
    def unite(self,x,y):
        x = self.find(x)
        y = self.find(y)

        #　もし親が同じなら結合は行わない。
        if x == y:
            return 0
        #　大きい木に小さい木を結合させる
        if self.par[x] > self.par[y]:
            x, y = y, x

        self.par[x] += self.par[y]
        self.par[y] = x


    # 再起関数で根を返す。
    def find(self,x):
        #x が根であった場合
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def same(self,x,y):
        return self.find(x) == self.find(y)


u = UnionFind(N)

for _ in range(M):
    a, b = map(int, input().split())
    if u.same(a, b):
        continue
    else:
        u.unite(a, b)

# print(u.par)
print(min(u.par)*-1)



