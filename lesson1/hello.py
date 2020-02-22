print("Привет мир!")
print("Hi proger!")
print(2 + 2)
print(285 / 15)

print()

while True:
    try:
        age = int(input('Сколько вам лет? '))
    except ValueError:
        print('недопустимый ввод!')
        continue
    break
  
birth_year = 2020 - age
print (f'Вы родились в {birth_year-1} или в {birth_year} году')
  