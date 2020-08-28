
num = int(input('Number: '))
divisors = list(filter(lambda x: num % x == 0, list(range(1, int(num/2 + 1)))))

def isperfectsquare(num):
    for i in range(2,num):
        if i ** 2 == num:
            return True
    return False


for i in divisors:
    if isperfectsquare(i):
        print(i)
        print('Not square free')
        break
else: 
    print('Its Square free')
