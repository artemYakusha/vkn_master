#6.1
import math as m
a = float(input('Введіть нижню границю: '))
b = float(input('Введіть верхню границю: '))
h = float(input('Введіть значення кроку: '))

for Bar in range(100):
    foo = m.fabs(m.tan(m.fabs(Bar)+0.1))
    print(foo)
    if Bar == b:
        break