from pprint import pprint
lst = []
count = 1
twos = 1
for rows in range(8):
    lst2 = []
    for cols in range(8):
        if count % 2 == twos:
            lst2.append(1)
        else: 
            lst2.append(2)
        count += 1
    lst.append(lst2)
    if twos == 1:
        twos = 0
    else:
        twos = 1
    

pprint(lst)
