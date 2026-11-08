text = input("введите текст: ")
words = text.split()

print("общее количество слов:", len(words))

print("частота слов:")
alreadyprinted = []
for w in words:
    if w not in alreadyprinted:
        print(w, ":", words.count(w))
        alreadyprinted.append(w)

maxw = ""
maxcount = 0
for w in words:
    if words.count(w) > maxcount:
        maxcount = words.count(w)
        maxw = w
print(" самое частое слово:", maxw)

shortest = words[0]
longest = words[0]
for w in words:
    if len(w) < len(shortest):
        shortest = w
    if len(w) > len(longest):
        longest = w
print("самое короткое слово:", shortest)
print("самое длинное слово:", longest)

newwords = []
for w in words:
    if len(w) >= 3:
        newwords.append(w)

print(" анализ после фильтрации ")
print("осталось слов:", len(newwords))

maxw2 = ""
maxcount2 = 0
for w in newwords:
    if newwords.count(w) > maxcount2:
        maxcount2 = newwords.count(w)
        maxw2 = w
print("самое частое слово:", maxw2)

shortest2 = newwords[0]
longest2 = newwords[0]
for w in newwords:
    if len(w) < len(shortest2):
        shortest2 = w
    if len(w) > len(longest2):
        longest2 = w
print("самое короткое слово:", shortest2)
print("самое длинное слово:", longest2)