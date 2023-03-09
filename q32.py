import random

n = int(input('Введите размер массива'))
min = int(input('Введите нижний предел'))
max = int(input('Введите верхний предел'))

arr = []
res = []
for i in range(n):
    arr.append(random.randint(-1000,1000))
    if (arr[i] >= min) and (arr[i] <= max):
        res.append(i)
        
print(res)