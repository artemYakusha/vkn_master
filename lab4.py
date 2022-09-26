import math as m
def func1(bar):
    foo1 = ((m.sin(bar) - m.log10(bar)) / ((7 * bar) ** 0.5)) + ((bar + 4) ** (2 * bar - 8))
    return foo1
bar1 = float(input('Введіть х '))
foo = func1(bar1)
print(foo)