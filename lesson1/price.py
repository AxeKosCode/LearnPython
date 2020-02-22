price = 100
discount = 5

price_with_discount = price - price * discount / 100

print(price_with_discount)

def discount_price(price, disc):
    return price - price * disc / 100

print(discount_price(100, 25))

while True:
    a = int(input ('Какая цена товара? '))
    if a <=0:
        print('Цена не может быть меньше 0!')
        continue
    break

i = 3
while i > 0:
    b = int(input ('Какую скидку желаете в % ? '))
    if b < 0 or int(b) > 100:
        print('Скидка некорректна! Дадим 0%')
        b = 0
        i -= 1
        continue
    break

result = discount_price(a, b)
print('Итоговая цена для Вас:', result, 'rub')
