# объявление функции
def is_prime(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return bool(count == 2)

def is_valid_password(password):
    password = password.split(':')
    palindrom_flag = False
    prime_flag = is_prime(int(password[1]))
    even_flag = False
    part_flag = False
    
    if len(password) == 3:
        part_flag = True    
    if list(password[0]) == list(reversed(password[0])):
        palindrom_flag = True
    if int(password[2]) % 2 == 0:
        even_flag = True
        
    if part_flag and palindrom_flag and prime_flag and even_flag:
        return True
    else:
        return False
    
    

# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))