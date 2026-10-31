categories = ["жилье", "питание", "транспорт", "развлечения"]
expenses = [0, 0, 0, 0]
total_income = 0

while True:
    print("--- финансовый помощник ---")
    print("1. добавить доход")
    print("2. добавить расход")
    print("3. показать анализ и рекомендации")
    print("4. выйти")

    choice = input("выберите пункт (1-4): ")

    if choice == "1":
        amount = float(input("введите сумму дохода: "))
        total_income += amount
        print("доход добавлен, общий доход теперь:", total_income)

    elif choice == "2":
        print("категории расходов:")
        print("1 - жилье, 2 - питание, 3 - транспорт, 4 - развлечения")
        cat = int(input("выберите номер категории (1-4): "))
        amount = float(input("введите сумму расхода: "))

        if 1 <= cat <= 4:
            expenses[cat - 1] += amount
            print("расход добавлен в категорию:", categories[cat - 1])
        else:
            print("ошибка: неверный номер категории")

    elif choice == "3":
        print("--- анализ ваших финансов ---")
        print("общий доход:", total_income, "руб.")

        total_expense = 0
        for i in range(4):
            if expenses[i] > 0:
                print("расходы на", categories[i], ":", expenses[i], "руб.")
                total_expense += expenses[i]

        print("общий расход:", total_expense, "руб.")

        balance = total_income - total_expense
        print("ваш баланс (остаток):", balance, "руб.")

        print("--- рекомендации ---")
        if total_income == 0:
            print("сначала добавьте доход, чтобы получить советы.")
        elif balance < 0:
            print("внимание! вы тратите больше, чем зарабатываете. срочно урежьте расходы.")
        else:
            max_exp = 0
            max_cat = ""
            for i in range(4):
                if expenses[i] > max_exp:
                    max_exp = expenses[i]
                    max_cat = categories[i]

            if max_exp > 0:
                print("самая большая трата — это", max_cat, "(", max_exp, "руб.)")
                print("попробуйте сократить её на 10%, чтобы сэкономить", max_exp * 0.1, "руб.")

            save = balance * 0.15
            print("рекомендуем откладывать 15% от остатка в сбережения — это", save, "руб.")

    elif choice == "4":
        print("до свидания!")
        break
    else:
        print("неверный пункт, попробуйте снова.")