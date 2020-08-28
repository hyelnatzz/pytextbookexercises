import random

sentence = 'sentence'.lower()
lst_sen = [i for i in sentence]
print(sentence)

len_lst = len(lst_sen)
pos_lst = []
new_sen_lst = []

while len(pos_lst) != len_lst:
    rand = random.randint(0,len_lst - 1)
    if rand not in pos_lst:
        pos_lst.append(rand)

for i in pos_lst:
    new_sen_lst.append(lst_sen[i])


print(''.join(new_sen_lst).capitalize())