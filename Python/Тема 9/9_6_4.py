s = input()
indStart = s.find('h')
indEnd = s.rfind('h')
part1 = s[:indStart + 1]
part2 = s[indEnd:]
part3 = s[indStart+1:indEnd]
rev = ''.join(reversed(part3))
new = part1+rev+part2
print(new)
