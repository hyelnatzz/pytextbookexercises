word = 'photosis'

def encrypt(word, key):
    dword = ''
    i = 0
    while len(dword) != len(word):
        dword += word[i::key]
        i += 1
    return dword



def decrypt(word, key):
    key += 2
    dword = ''
    i = 0
    while len(dword) != len(word):
        dword += word[i::key]
        i += 1
    return dword


word = encrypt(word, 3)
dword = decrypt(word, 3)

print('E=', word, 'D=', dword)
