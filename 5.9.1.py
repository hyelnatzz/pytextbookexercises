count = len(list(filter(lambda x: (x**2)%10 == 1, range(100))))



new_count = 0

for i in range(100):
    if (i**2) % 10 == 1:
        print(i**2, end=' ')
        new_count += 1
print()
print(count)
print(new_count)