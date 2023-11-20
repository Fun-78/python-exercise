'''
import math

num = float(input("Enter a number: "))
if num >= 0:
    root = math.sqrt(num)
    print(f"The square root of {num} is {root}")
else:
    print(" the number is negative")
    '''

# 2.
'''
w1 = input("Enter the first word: ")
w2 = input("Enter the second word: ")
if w1 < w2:
    print(f"The smallest word is: {w1}")
else:
    print(f"The smallest word is: {w2}")
#ternary instruction
print(f"The smallest word is: {w1 if w1 < w2 else w2}")
'''

# 3.

pSeuil = 2.1
vSeuil = 7.41
pressure = float(input('enter the pressure: '))
volume = float(input('enter the vloume: '))
if pressure > pSeuil and volume >vSeuil:
    print('immediate stop')
elif pressure > pSeuil:
    print('increase the volume of enclosure')
elif volume > vSeuil:
    print('reduce the speaker volume')
else:
    print('everything is fine')


