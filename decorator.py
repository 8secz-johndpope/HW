# декоратор с аргументами оборачиваемой функции
def square(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if isinstance(res,(float,int)):
            return res ** 2
        return []
    return wrapper

# декоратор, который сам может принимать аргументы
def pow(power):
    def decorator(func):
        def wrapper(*args, **kwargs):
            res = 1
            if isinstance(func(*args,**kwargs),(float,int)):
                for i in range(power):
                    res *= func(*args, **kwargs)
                return res
            return []
        return wrapper
    return decorator

@square
def f2(a):
        return a

@pow(power=3)
def f3(c, g):
    if isinstance(c, (float, int)) and isinstance(g,(float,int)):
        return c - g
    return []

