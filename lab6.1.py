#6.1
import math as m
a = float(input('Введіть нижню границю: '))
b = float(input('Введіть верхню границю: '))
h = float(input('Введіть значення кроку: '))

for Bar in range(1, 100):
    foo = m.log(3, m.fabs(Bar + m.e**Bar))
    print(foo)
    if Bar == b:
        break