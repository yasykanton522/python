import time

def timing(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print("Время:", (end - start) * 1000, "мс")
        return res
    return wrapper

@timing
def test():
    for i in range(1000000):
        pass

test()