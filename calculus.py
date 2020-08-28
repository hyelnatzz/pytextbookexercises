eq = 'x20'
"""exp = 0
eqn = ''
val = ''
alpha = ''

if eq[0].isalpha():
    alpha = eq[0]
    exp = int(eq[1:])
    val = 1
else:
    for i in eq:
        if i.isnumeric():
            val += i
        else: 
            alpha = i
            exp = int(eq[eq.find(i)+1:])
            break
    val = int(val)
print(exp)
print(val)

eqn = str(exp * val) + alpha + str(exp - 1)
print(eqn)"""

eq = 'x^6'

val, exp = eq.split('^')
strt = ''
exp = int(exp)
if val.isalnum():
    for i in val:
        if i.isnumeric():
            strt += i
        else:
            strt = '1'
            break
    strt = int(strt)
eqn = str(strt * exp) + 'x^'+ str(exp - 1)
print(eqn)