import random
a = random.randint(1,100)
while True :
    b=int(input("ведите свое предположение: "))
    if b==a :
        print("угадал!!!")
        break
    elif b>a :
        print("меньше")
    else :
        print ("больше")
