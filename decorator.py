# декоратор с аргументами оборачиваемой функции
def square(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return res ** 2
    return wrapper

# декоратор, который сам может принимать аргументы
def pow(power):
    def decorator(func):
        def wrapper(*args, **kwargs):
            res = 1
            for i in range(power):
                res *= func(*args, **kwargs)
            return res
        return wrapper
    return decorator

@square
def f2(a):
    return a

@pow(power=3)
def f3(c, g):
    return c - g

print(f2(1, 3, 0))
print(f3(10, 7))
