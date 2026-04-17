def n_squared(n):
    sonion = dict()
    for i in range(1, n + 1):
        sonion[i] = i ** 2

    print(sonion)

son = {'c1': 'Red', 'c2': 'Green', 'c3': None}
def drop_ts(dic):
    new_dic = {}
    for key, value in dic.items():
        if value is not None:
            new_dic[key] = value

    print(new_dic)