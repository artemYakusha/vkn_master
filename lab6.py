#6.1
import math as m
a = float(input('Введіть нижню границю: '))
b = float(input('Введіть верхню границю: '))
h = float(input('Введіть значення кроку: '))

for Bar in range(a, b, h):
    foo = m.fabs(m.tan(m.fabs(Bar)+0.1))
    print(foo)
#6.2
import math as m
a = float(input('Введіть нижню границю: '))
b = float(input('Введіть верхню границю: '))
h = float(input('Введіть значення кроку: '))

spisok = [[], []]
while a < b:
    spisok[1].append(m.fabs(m.tan(m.fabs(a)+0.1)))
    spisok[0].append(a)
    a += h
l = len(spisok)

#6.3 v1
Foo = 0
while Foo != len(spisok[0]):
    print(spisok[0][Foo])
    Foo += 1
Foo1 = 0
while Foo1 != len(spisok[1]):
    print(spisok[1][Foo1])
    Foo1 += 1

print(spisok)

spisok1 = []
for BAR in range(l):
    spisok1.append(spisok[1][BAR] * spisok[0][BAR])
print(spisok1)

#6.3 v2
x=1
for item in spisok[0]:
    x*=item

y=1
for item in spisok[1]:
    y *= item

new_list = [x, y]

print(new_list)