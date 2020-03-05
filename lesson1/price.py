price = 100
discount = 5

price_with_discount = price - price * discount / 100

print(f'цена: {price} rub, скидка: {discount} %. \nИтоговая сумма: {price_with_discount} rub')
print()

def discount_price(price, disc):
    return price - price * disc / 100

print('*проверка вызова функции с аргументами 100 и 25*', discount_price(100, 25))
print()

print('Сейчас мы рассчитаем итоговую цену товара на основе Ваших данных.\n')
while True:
    try:
        a = int(input ('Какая цена товара? '))
    except TypeError:
        print('Пожалуйста, введите цену цифрами!\n')
        continue
    except ValueError:
        print('Пустое значение недопустимо!\n')
        continue
    if a <= 0:
        print('Извините, но мы не раздаём товары бесплатно!\n')
        continue
    break

i = 2
while i > 0:
    try:
        b = abs(int(input ('Какую скидку желаете в % ? ')))
    except TypeError:
        print('Пожалуйста, введите скидку цифрами!\n')
        i -= 1
        continue
    except ValueError:
        print('Пустое значение недопустимо!\n')
        continue
    if b >= 100:
        print('Значение некорректно!\n')
        b = 0
        i -= 1
        continue
    break

result = discount_price(a, b)
print(f'\nИтоговая цена для Вас: [ {result} ] rub')
