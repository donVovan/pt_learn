#s = '2 4 3'.split()#input()
#for i in s:
#    i = int(i) ** 3
#    print(i, end=' ')
#cub = [int(i) ** 3 for i in input().split()]
print(*[int(i) ** 3 for i in input().split()], end=' ')