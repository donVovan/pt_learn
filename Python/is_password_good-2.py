# объявление функции
def is_password_good(password):
    if (any(x.isupper() for x in password) and any(x.islower() for x in password) and any(x.isdigit() for x in password) and len(password) >= 8):
        return True
    else:
        return False
     
        
        

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))