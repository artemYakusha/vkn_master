import math


def fun(x):
    return math.exp(x) + math.sqrt(math.fabs(x))


a=int(input("Введіть нижню границю: "))
b=int(input("Введіть верхню границю: "))
h=int(input("Введіть крок: "))

list_items=[[], []]

for i in range(a, b, h):
    list_items[0].append(i)
    list_items[1].append(fun(i))
x=1
for item in list_items[0]:
    x*=item

y=1
for item in list_items[1]:
    y*=item

new_list=[x, y]

print(new_list)