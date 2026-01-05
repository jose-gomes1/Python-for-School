def decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Dando run do Decorator com os parametros: {args} e {kwargs}")
        result = func(*args, **kwargs)
        return func
    return wrapper

@decorator
def func(a, b):
    print(f"{a} e {b} existem")

func("test", "test2")