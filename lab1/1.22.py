def type_check(*types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(len(args)):
                if type(args[i]) != types[i]:
                    raise TypeError(f"Аргумент {i+1} должен быть {types[i]}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@type_check(int, int)
def add(a, b):
    return a + b

print("Сумма:", add(5, 10))