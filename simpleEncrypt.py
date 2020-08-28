word = input('Word: ')


def encrypt(word):
    p1 = word[::2]
    p2 = word[1::2]
    return p1 + p2


def decrypt(word):
    middle = int(len(word)/2)
    if len(word) % 2 == 1:
        p1 = word[:middle+1]
        p2 = word[middle+1:] + ' '
    else:
        p1 = word[:middle]
        p2 = word[middle:]
    new_word = ''

    for i in range(len(p1)):
        new_word += p1[i]+p2[i]
    return new_word

encrypted = encrypt(word)
print('Encrypted=', encrypted, 'Decrypted=', decrypt(encrypted))
