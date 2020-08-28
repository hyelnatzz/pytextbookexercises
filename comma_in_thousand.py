
num = input('Enter Num:  ')
new_num = ''

num = num[::-1]

for i in range(len(num)):
    if i % 3 == 0:
        new_num += ','
    new_num += num[i]

new_num = new_num[::-1][:-1]

print(new_num)