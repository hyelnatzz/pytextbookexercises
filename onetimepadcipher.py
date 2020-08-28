import string
import random
import sys

alpha = string.ascii_lowercase
punct = string.punctuation


def encrypt(word,shift):
    eword = ''
    for i in word:
        if i == ' ':
            eword += ' '
            continue
        if i in punct:
            eword += i
            continue
        pos = alpha.find(i)
        shift_num = pos + shift
        if shift_num > len(alpha) - 1:
            shift_num -= len(alpha)
        eword += alpha[shift_num]
    return eword

def decrypt(word, shift):
    dword = ''
    for i in word:
        if i == ' ':
            dword += ' '
            continue
        if i in punct:
            dword += i
            continue
        pos = alpha.find(i)
        shift_num = pos - shift
        if shift_num < 0:
            shift_num += len(alpha)
        dword += alpha[shift_num]
    return dword
    
def otp_enc(word, lst):
    pos = 0
    eword = ''
    for i in word:
        eword += encrypt(i,lst[pos])
        pos += 1
    return eword


def otp_dec(word, lst):
    pos = 0
    dword = ''
    for i in word:
        dword += decrypt(i, lst[pos])
        pos += 1
    return dword


word = input('Word or Sentence to Encrpyt: ').lower()
lst = [random.randint(0, len(alpha) - 1) for i in range(len(word))]


otpw = otp_enc(word, lst)
dotpw = otp_dec(otpw, lst)

print('Encrypted:=>  ', otpw)
print('Decrypted:=>  ', dotpw)
