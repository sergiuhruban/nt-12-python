def f1(*args: object, **kwargs: object) -> object:
    s = 0

    for param in args:
        if type(param) == int or type(param) == float:
            s += param

    return s


print(f1(1, 5, -3, 'abc', [12, 56, 'cad']))
print(f1())
print(f1(2, 4, 'abc', param_1=2))