def cache(func):
    kesh = {}
    def wrapper(*args):
        if args in kesh:
            print("Из кэша")
            return kesh[args]
        print("Вычислено")
        res = func(*args)
        kesh[args] = res
        return res
    return wrapper
@cache
def umnozh(a, b):
    return a * b
print(umnozh(5, 3))
print(umnozh(5, 3))