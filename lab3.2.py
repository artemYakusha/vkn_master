import sys
bar = sys.argv[1]
foo = ((float(bar) ** 2)/4)/3.14
sys.stdout.write('площа кола = ')
sys.stdout.write(str(foo))