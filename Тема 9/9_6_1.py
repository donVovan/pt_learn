a = int(input())
b = int(input())
s = ''
for i in range(a, b + 1):
    s += chr(i)
print(' '.join(s))
