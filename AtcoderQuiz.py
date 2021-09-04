dic = {'ABC':True, 'ARC':True, 'AGC':True, 'AHC':True}

for _ in range(3):
    s = input()
    dic[s] = False

for key in dic.keys():
    if dic[key]:
        print(key)
