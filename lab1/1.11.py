age = int(input("возраст: "))
income = int(input("доход в месяц: "))
credit = int(input("сумма кредита: "))
months = int(input("на сколько месяцев кредит: "))
history = input("кредитная история (отличная/хорошая/плохая): ")
guarantors = input("поручители (да/нет): ")
collateral = input("залог (да/нет): ")

payment = credit / months
print("платеж в месяц составляет", payment)

nagruzka = payment / income * 100
print("нагрузка относительно дохода", nagruzka, "%")

if history == "плохая" or nagruzka > 50:
    print("риск: критический")
    print("ставка: 25%")
    print("решение: отклонить")
elif history == "хорошая" and (guarantors == "да" or collateral == "да") and nagruzka < 30:
    print("риск: низкий")
    print("ставка: 12%")
    print("решение: одобрить")
else:
    print("риск: средний")
    print("ставка: 18%")
    print("решение: одобрить с условиями")