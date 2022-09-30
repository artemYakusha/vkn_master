#1
s1 = input('Перший рядок  ')
s2 = input('Другий рядок  ')
s3 = ''
for i in s1:
    if i in s2:
        s3 += i
print(s3)

