s = int(input('введите число'))
k = 0
while s>0:
    k+=1
    s = s//10
print('кол-во символов = ',k)
print(chr(64+k))

