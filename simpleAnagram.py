import random

word = input('Word: ')
pos = []

while len(pos) != len(word):
    num = random.randint(0,len(word)-1)
    if num not in pos:
        pos.append(num)

new_word = ''
for i in pos:
    new_word += word[i]
print(new_word)