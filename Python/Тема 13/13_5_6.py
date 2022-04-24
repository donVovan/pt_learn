# объявление функции
def is_palindrome(text):
    text = text.lower()
    arr = []
    for i in range(len(text)):
        if text[i].isalpha():
            arr.append(text[i])
    if arr == list(reversed(arr)):
        return True
    else:
        return False
         

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))