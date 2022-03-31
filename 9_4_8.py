s = input()
start = s.find('h')
finish = s.rfind('h') + 1
new_string = s[:start] + s[finish:]
print(new_string)
