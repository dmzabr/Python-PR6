a1 = int(input('Введите первый элемент прогрессии'))
d = int(input('Введите разность прогрессии'))
n = int(input('Введите количество элементов'))

array = [a1]

for i in range (n-1):
    array.append(array[i]+d)
    
print(array)