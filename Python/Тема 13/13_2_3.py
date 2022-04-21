# объявление функции
def print_digit_sum(num):
    num = str(num)
    num_sum = 0
    for i in range(len(num)):
        num_sum += int(num[i])
    print(num_sum)
        
# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)