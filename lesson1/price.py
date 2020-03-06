price = 100
discount = 5
max_discount = 49

price_with_discount = price - price * discount / 100

print(f'цена: {price} rub, скидка: {discount} %. \nИтоговая сумма: {price_with_discount} rub')
print()

def discount_price(price, disc):
    return price - price * disc / 100

print('* проверка вызова функции с аргументами 100 и 25.   Ответ:', discount_price(100, 25))
print('\n\n')


def user_input_for_price():
    print('Сейчас мы рассчитаем итоговую цену товара на основе Ваших данных.\n')
    while True:
        try:
            a = round(abs(float(input ('Какая цена товара? '))), 2)
        except ValueError:
            print('(!) Пожалуйста, введите цену цифрами!\n')
            continue
        if a <= 0:
            print('Извините, но мы не раздаём товары бесплатно!\n')
            continue
        break
    return a

def user_input_for_discount(max_disc = max_discount):
    i = 2
    while i > 0:
        try:
            b = round(abs(float(input (f'Какую скидку желаете (в %)? \n(Максимально возможная скидка {max_disc}%) '))), 2)
        except ValueError:
            i -= 1
            if i:
                print('(!) Пожалуйста, введите скидку цифрами!')
                continue
            else:
                b = 0
        break

    if b > max_disc:
        print(f'{b}% ??? Извините, но мы не можем на это пойти!')
        b = max_disc
    if b < 0.1:
        b = 0
    print(f'\nДля Вас применена скидка {b}%')
    return b


result = round(discount_price( user_input_for_price(), user_input_for_discount() ), 2 )
itog = '\n  ' + '='*(27 + len(str(result))) + '\n'
print(itog + f'    Итоговая цена: [ {result} ] rub' + itog)
