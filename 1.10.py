sum = int(input("Сумма покупки: "))
age = int(input("Ваш возраст: "))
HP = int(input("У вас сегодня день рождения? (1 - да, 0 - нет): "))
VIP = int(input("Вы VIP-клиент? (1 - да, 0 - нет): "))
sale = 0
sale1 = 0
if sum > 1000:
    sale += 10
if age >= 63:
    sale += 5
if HP == 1:
    sale += 5
if VIP == 1:
    sale1 = 15
if sale > sale1:
    sale2 = sale
else:
    sale2 = sale1
if sale2 > 25:
    sale2 = 25
print(sale2, "% составляет ваша скидка")