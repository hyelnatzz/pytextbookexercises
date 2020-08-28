import random
num_lst = [1,1,0,0,1,0,1,0,1,0,0,0,1] #[random.randint(0,1) for i in range(100)]
"""
mx = 0
cur = 0
for i in num_lst:
    if i == 0:
        cur += 1
        if cur > mx:
            mx = cur
    else:
        cur = 0

print(mx)
"""
new_lst = []

for i in num_lst:
    if i not in new_lst:
        new_lst.append(i)

print(new_lst)