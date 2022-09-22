import math
bar = float(input('Введіть число х:  '))
def f1(bar1):
    rez = "тут первый выраз системы"
    return (rez)
def f2(bar2):
    rez = "тут второй"
    return (rez)
def f3(bar3):
    rez = "тут третий"
    return (rez)
y = 0.0
if "первое условия":
    y = f1(bar)
elif "второе условие":
    y = f2(bar)
else:
    y = f3(bar)
print(int(y))

#5.2
a1 = 7
a2 = 10
a3 = 4
bar = int(input('Введіть N  '))
foo1 = bar/a1
Foo1 = foo1 / (int(foo1))
foo2 = bar/a2
Foo2 = foo2 / (int(foo2))
foo3 = bar/a3
Foo3 = foo3 / (int(foo3))
if Foo1 == 1 and Foo2 == 1 and Foo3 == 1:
    print('це спільне кратне для всіх чисел')
elif Foo1 == 1 and Foo2 == 1:
    print('це спільне кратне тільки для а1 та а2')
elif Foo1 == 1 and Foo3 == 1:
    print("це спільне кратне тільки для а1 та а3")
elif Foo2 == 1 and Foo3 == 1:
    print("це спільне кратне тільки для а2 та а3")
elif Foo1 == 1:
    print("це спільне кратне тільки для а1")
elif Foo2 == 1:
    print("це спільне кратне тільки для а2")
elif Foo3 == 1:
    print("це спільне кратне тільки для а3")
else:
    print('це не є спільне кратне для жодного числа')