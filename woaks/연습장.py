def one(custom_function):
    def two():
        print('전')
        custom_function()
    return two

def f():
    print('hello world')

print(one(f)())