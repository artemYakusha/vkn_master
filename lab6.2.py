import math as m
a = float(input('Введіть нижню границю: '))
b = float(input('Введіть верхню границю: '))
h = float(input('Введіть значення кроку: '))

spisok = [[], []]
while a < b:
    spisok[1].append(m.fabs(m.tan(m.fabs(a)+0.1)))
    spisok[0].append(a)
    a += h
