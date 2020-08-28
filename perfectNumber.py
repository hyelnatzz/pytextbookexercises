
num_list = []

for i in range(1,10001):
    num = i
    divisors = list(filter(lambda x: num % x == 0, list(range(1,int(num/2 + 1)))))
    if sum(divisors) == num:
        num_list.append(num)

print(num_list)