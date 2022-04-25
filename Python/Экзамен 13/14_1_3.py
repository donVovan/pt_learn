from math import factorial
# объявление функции
def compute_binom(n, k):
    F = factorial(n) / (factorial(k) * factorial(n - k))
    return int(F)

# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))