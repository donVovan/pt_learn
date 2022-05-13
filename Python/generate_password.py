from random import *

from random import *
def generate_password(length, chars):
    password = ''
    for i in range(length):
        i = choice(chars)
        password += i
    return password

digits = '23456789'
lowercase_letters = 'abcdefghjkmnpqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKMNPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
exc = 'il1Lo0O'
chars = ''
result = []
how_many = int(input('Введите сколько паролей нужно сгенерировать? '))
length = int(input('Введите длину одного пароля? '))
numbers = input('Включать цифры? "y" или "n" ')
big_letters = input('Включать прописные буквы? "y" или "n" ')
sm_letters = input('Включать строчные буквы? "y" или "n" ')
symb = input('Включать символы? "y" или "n" ')
simple = input('Включать неоднозначные например (il1Lo0O) символы? "y" или "n" ')


if numbers.lower() == 'y':
    chars += digits
if big_letters.lower() == 'y':
    chars += uppercase_letters
if sm_letters.lower() == 'y':
    chars += lowercase_letters
if symb.lower() == 'y':
    chars += punctuation
if simple.lower() == 'y':
    chars += exc
    
for i in range(how_many):
    result.append(generate_password(length, chars))
print()
for j in result:
    print(j)
