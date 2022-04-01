n = int(input())
message = input()
for i in message:
    descrypt = ord(i) - n
    if descrypt < 97:
        descrypt += 26
    print(chr(descrypt), end='')
        
