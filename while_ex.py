import sys
from typing import Counter
"""count = 0

while count <= 50:
    print(count)
    count += 1"""

"""wrd = 'word'

count = 0
#using try instead of len()
try:
    while count < 100:
        print(wrd[count])
        count += 1
except :
    print('done')"""

#every second xter ==> instead of print(word[::2])
"""wrd = 'word'

count = 0
try:
    while count < 100:
        if count % 2 == 0:
            print(wrd[count + 1])
        count += 1
except:
    print('done')"""
"""wrd = 'word'
print(wrd[1::2])"""
#password retries
"""mx = 5
count = 0
pword = 'password'
upword = input('Password: ')
correct = False

while not correct:
    count += 1
    if upword == pword:
        correct = True
        print('Logged IN!!')
        break
    if count == mx:
        print('You have reached max, Good bye')
        break
    if mx - count == 1:
        print('Incorrect password, you have', mx - count, 'retry left.')
    else:
        print('Incorrect password, you have', mx - count,'tries left.')
    upword = input('Password: ')

    
print('done')"""
#A's in score
"""
scores = []
score = int(input('Enter scores: '))
a_s = 0
if score < 0:
    print('its over even before its started')
    sys.exit()

while score > 0:
    scores.append(score)
    score = int(input('Enter scores enter "-1" to quit: '))

for i in scores:
    if i >= 90:
        a_s +=1 

avg = sum(scores)/len(scores)

print('there are', a_s, 'A"s and the average of the score is', avg)
"""

word = 'string'
lt = 'n'
ln = len(word)
count = 0
while count < ln:
    if word[count] == lt:
        print(count)
        break
    count += 1

