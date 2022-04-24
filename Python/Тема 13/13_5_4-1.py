# объявление функции
def is_password_good(password):
    if len(password) < 8:
        return False
    upper = False
    lower = False
    digit = False
    for i in password:
        if i.isupper():
            upper = True
        if i.islower():
            lower = True
        if i.isdigit():
            digit = True
    if upper == True and lower == True and digit == True:
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))