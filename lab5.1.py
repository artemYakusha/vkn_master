import math as m
bar1 = float(input('Введіть число х:  '))
def f1(bar):
    rez = 2.27 * m.e ** (4*bar+1) + 3
    return rez
def f2(bar):
    rez = 0.64 * bar ** (bar+1)
    return rez
def f3(bar):
    rez = m.log(bar) * m.fabs(bar - m.e ** bar)
    return rez
y = 0.0
if bar1 > 7:
    y = f1(bar1)
elif 0.5 < bar1 <= 7:
    y = f2(bar1)
else:
    y = f3(bar1)
print(y)
