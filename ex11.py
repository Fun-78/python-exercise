'''
def cube(n):
    return n**3
cube(3)


import math 

def cube(number): 
    return math.pow(number, 3) # number ** 3
    '''

import math
def cube(n):
    return n ** 3
def volumesphere(r):
    return 4/3 * math.pi *cube(r)
print(volumesphere)