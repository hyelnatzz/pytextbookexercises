import random


for i in range(10):
    x = random.randint(1,10)
    y = random.randint(1, 10)
    ans =  int(input(f'{x} x {y} = '))
    if ans == x * y:
        print('Right!!!')
    else:
        print(f'Wrong. The answer is {x*y}')
