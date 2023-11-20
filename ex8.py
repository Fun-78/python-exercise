import math
for  x in range(-3,4):
    try:
        value = math.sin(x) / x
        print(f'for x = {x}, sin(x)/ = {value}')
    except ZeroDivisionError:
        print('for x = 0, sin(x)/x is undefined')