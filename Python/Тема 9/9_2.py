s = input()
if len(s) % 2 != 0 and len(s) > 1:
    d = len(s) // 2
    part1 = s[:d+1]
    part2 = s[d+1:]
    print(part2+part1)
elif len(s) % 2 == 0:
     d = len(s) // 2
     part1 = s[:d]
     part2 = s[d:]
     print(part2+part1)
else:
    print(s)

