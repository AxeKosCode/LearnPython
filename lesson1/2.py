list = [3,5,7,9,10.5]
print(list)
list.append('Python')
print(list)
print('Длина списка = ', len(list))

print('Первый эл-т', list[0])
print('Последний эл-т', list[-1])
print('Срез 2:5', list[2:5])
list.remove('Python')
print('Удалили "Python". Теперь список =', list)

