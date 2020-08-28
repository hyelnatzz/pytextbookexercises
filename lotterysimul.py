import random


lot_num = []
correct = 0
user_drawn = []
pos = []

while len(lot_num) != 6:
    num = random.randint(1,10)
    if num not in lot_num:
        lot_num.append(num)

for i in range(1000000):
    while len(user_drawn) != 6:
        num = random.randint(1, 10)
        if num not in user_drawn:
            user_drawn.append(num)
    if user_drawn == lot_num:
        correct += 1
        pos.append(i)
    print(i, user_drawn,' ===> ', lot_num)
    user_drawn = []

print(pos, correct)
