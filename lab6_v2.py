import math


def fun(x):
    return math.exp(x) + math.sqrt(math.fabs(x))


a=float(input("Введіть нижню границю: "))
b=float(input("Введіть верхню границю: "))
h=float(input("Введіть крок: "))

list_items=[[], []]

for i in range(100):
    list_items[0].append(i)
    list_items[1].append(fun(i))
    if i == b:
        break
print(list_items)

# Вариант 1

x=1
for item in list_items[0]:
    x*=item

y=1
for item in list_items[1]:
    y*=item

new_list=[x, y]

print(new_list)

# Вариант 2

new_list=[]

for i in range(len(list_items[0])):
    new_list.append(list_items[0][i] * list_items[1][i])

print(new_list)
for i in range(100):
    pass
for i in range (1,2,1):
    pass
for i in list_items:
    pass