n = int(input())
x_list = []
f = []
for i in range(1, n + 1):
    x = int(input())
    x_list.append(x)
    f.append(x ** 2 + 2 * x + 1)
print(*x_list, sep='\n')
print()
print(*f, sep='\n')
