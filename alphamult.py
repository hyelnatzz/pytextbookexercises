l1 = [2,3,5]
l2 = [4,3,6]
l3 = []

for i,j in zip(l1,l2):
    l3.append(i+j)

print(l3)