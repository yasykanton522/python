text = input("введите числа через пробел: ")
parts = text.split()

numbers = []
for p in parts:
    numbers.append(float(p))

print("уникальные:", " ")
seen = []
for n in numbers:
    if n not in seen:
        print(n, " ")
        seen.append(n)

print("\nповторяющиеся:", " ")
seen2 = []
for n in numbers:
    if numbers.count(n) > 1 and n not in seen2:
        print(n, " ")
        seen2.append(n)
print("\nчетные:", " ")
for n in numbers:
    if n % 2 == 0:
        print(n, " ")
print("\nнечетные:", " ")
for n in numbers:
    if n % 2 != 0:
        print(n, " ")
print("\nотрицательные:", " ")
for n in numbers:
    if n < 0:
        print(n, " ")
print("\nс плавающей точкой:", " ")
for n in numbers:
    if n != int(n):
        print(n, " ")
sum5 = 0
for n in numbers:
    if n % 5 == 0:
        sum5 += n
print("\nсумма кратных 5:", sum5)
print("самое большое:", max(numbers))
print("самое маленькое:", min(numbers))