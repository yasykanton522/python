names = ["смартфон", "наушники", "смартфон", "ноутбук", "наушники"]
prices = [500, 150, 500, 1200, 150]
qtys = [2, 5, 1, 3, 2]
uniquenames = []
for n in names:
    if n not in uniquenames:
        uniquenames.append(n)
print("выручка по товарам:")
for u in uniquenames:
    total = 0
    for i in range(len(names)):
        if names[i] == u:
            total += prices[i] * qtys[i]
    print(u, ":", total)
maxname = ""
maxrev = 0
for u in uniquenames:
    total = 0
    for i in range(len(names)):
        if names[i] == u:
            total += prices[i] * qtys[i]
    if total > maxrev:
        maxrev = total
        maxname = u
print("самый прибыльный товар:", maxname)
print("количество уникальных наименований:", len(uniquenames))