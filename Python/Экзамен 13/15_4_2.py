from random import *
def generate_password(length, chars):
    password = ''
    for i in range(length):
        i = choice(chars)
        password += i
    return password
nabor = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXY!#$%&*+-=?@^_Z0123456789'
dlina = 8
print(generate_password(dlina, nabor))
