def is_prime(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return bool(count == 2)

def get_next_prime(num):
    new_prime = num + 1
    while is_prime(new_prime) == False:
        new_prime += 1
    return new_prime
        
    

# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))