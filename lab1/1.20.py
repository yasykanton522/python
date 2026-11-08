def unique_elements(vlozh):
    result = []

    def proverka(spisok):
        for el in spisok:
            if type(el) == list:
                proverka(el)  # Рекурсия
            else:
                if el not in result:  # Проверка на дубликат
                    result.append(el)

    proverka(vlozh)
    return result
list_a = [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2, 3]]]]
print("Уникальные элементы:", unique_elements(list_a))