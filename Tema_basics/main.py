# problema functie recursiva
def Sum_(n):
    if n <= 1:
        return n
    else:
        return n + Sum_(n - 1)

n = 16
print(Sum_(n))

def sum_even(n):
    if n == 0:
        return 0
    if not n % 2 == 0:
        return sum_even(n-1)
    else:
        return n + sum_even(n-1)

n = 2
print(sum_even(n))

def sum_odd(n):
    if n <= 0:
        return 0
    if n % 2 == 0:
        return sum_odd(n-1)
    else:
        return n + sum_odd(n-2)

n = 7
print(sum_odd(n))

# problema functie citire de la tastura
try:
    number = (int(input("Choose number:")))
    print(number)

except ValueError:
    print(0)

# problema functie numar nedefinit de parametri

def param(*args, **kwargs):
    s = 0
    if type(kwargs) == int:
        s += kwargs
    for x in args:
        if type(x) == int or type(x) == float:
            s += x
    return s

print(param(1, 5, -3, 'abc', [12, 56, 'cad']))
print(param())
print(param(2, 4, 'abc', kwargs=2))

