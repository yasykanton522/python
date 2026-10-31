import datetime

def log_calls(file):
    def decorator(func):
        def wrapper(a, b):
            now = datetime.datetime.now()
            with open(file, "a", encoding="utf-8") as f:
                f.write(str(now) + " | " + func.__name__ + " | аргументы: " + str(a) + ", " + str(b) + "\n")
            return func(a, b)
        return wrapper
    return decorator

@log_calls("log.txt")
def summa(a, b):
    return a + b

print("Сумма:", summa(5, 10))