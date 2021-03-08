
def add_ten(x):
    return x+10
def twice(func,arg):
    return func(func(arg))
print(twice(add_ten,10))

def add (x):
    return x + 20
def twice(fun,arg):
    return fun(fun(arg))
print(twice(add,10))