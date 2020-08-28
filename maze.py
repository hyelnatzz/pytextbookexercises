import string
import random
import sys
from pprint import pprint

xters = string.ascii_lowercase+ string.ascii_uppercase + string.punctuation

xters_list = [i for i in xters]

cols = 10
rows = 10
choosen_xters = []
c = 0
while len(choosen_xters) != int(rows*cols/2):
    choice = random.choice(xters_list)
    if choice not in choosen_xters:
        choosen_xters.append(choice)
        c += 1
        print(c)

def shuffle(lst):
    print('shuffling...')
    shf = []
    while len(shf) != len(lst):
        rd = random.choice(lst)
        if rd not in shf:
            shf.append(rd)

    return shf


new_outcome = []
trk_lst = []
selected = []


while len(new_outcome) != rows:
    while len(trk_lst) != cols:
        for rd in choosen_xters:
            if selected.count(rd) < 2 and rd not in trk_lst:
                selected.append(rd)
                trk_lst.append(rd)
                if len(trk_lst) == cols:
                    break
    new_outcome.append(shuffle(trk_lst))
    trk_lst = []


pprint(shuffle(new_outcome))
