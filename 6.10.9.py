"""def isperfectsquare(num):
    for i in range(2, num):
        if i ** 2 == num:
            return True
    return False


def isperfectcube(num):
    for i in range(2, num):
        if i ** 4 == num:
            return True
    return False


def isperfectfifth(num):
    for i in range(2, num):
        if i ** 5 == num:
            return True
    return False

counted = []
count = 0
for i in range(1,1001):
    if isperfectfifth(i) or isperfectcube(i) or isperfectsquare(i):
        continue
    count += 1
"""
counted = []
count = 0
for i in range(1, 1000):
    if i**2 <= 1000 or i**4<=1000 or i ** 4<= 1000:
        continue
    count += 1

print(count)




