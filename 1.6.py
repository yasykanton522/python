a = int(input("введите день рождения: "))
b = int(input("введите месяц рождения: "))

if a < 1 or a > 31 or b < 1 or b > 12:
    print("вы опечатались")
else:
    if (21 <= a <= 31 and b == 3) or (1 <= a <= 19 and b == 4):
        print("вы овен")
    elif (20 <= a <= 30 and b == 4) or (1 <= a <= 20 and b == 5):
        print("вы телец")
    elif (21 <= a <= 31 and b == 5) or (1 <= a <= 20 and b == 6):
        print("вы близнецы")
    elif (21 <= a <= 30 and b == 6) or (1 <= a <= 22 and b == 7):
        print("вы рак")
    elif (23 <= a <= 31 and b == 7) or (1 <= a <= 22 and b == 8):
        print("вы лев")
    elif (23 <= a <= 31 and b == 8) or (1 <= a <= 22 and b == 9):
        print("вы дева")
    elif (23 <= a <= 30 and b == 9) or (1 <= a <= 22 and b == 10):
        print("вы весы")
    elif (23 <= a <= 31 and b == 10) or (1 <= a <= 21 and b == 11):
        print("вы скорпион")
    elif (22 <= a <= 30 and b == 11) or (1 <= a <= 21 and b == 12):
        print("вы стрелец")
    elif (22 <= a <= 31 and b == 12) or (1 <= a <= 19 and b == 1):
        print("вы козерог")
    elif (20 <= a <= 31 and b == 1) or (1 <= a <= 18 and b == 2):
        print("вы водолей")
    elif (19 <= a <= 28 and b == 2) or (1 <= a <= 20 and b == 3):
        print("вы рыбы")