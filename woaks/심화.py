def one(x):
    def two(y):
        return x ** y
    return two

f1 = one(2)
f1(3)
f1(4)

f2 = one(3)
f2(3)
f2(4)

def decorator(custom_function):
    def wrapper():
        print('전')
    return wrapper

@decorator
def f():
    print('hello world')

def one(custom_function):
    def two():
        print('전')
    return two

@one
def f():
    print('hello world')

f()