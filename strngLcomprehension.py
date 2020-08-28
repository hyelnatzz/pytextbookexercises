lst_str = ['is', 'a','Hello', 'Best', 'Crazy']

no_1st = [i[1:] for i in lst_str]
len_lst = [len(i) for i in lst_str]

least_3 = [x for x in lst_str if len(x) >= 3]

lst = [no_1st, len_lst, least_3]

for i in lst:
    print(i)
