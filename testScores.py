num1 = input('String1: ')
num2 = input('String2: ')
new = ''
count = 0

if len(num1) == len(num2):
    for i,j in zip(num1, num2):
        new += i+j

print(new)
