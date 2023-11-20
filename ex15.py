def sum(a,b,c):
    return a + b + c
num = (1,2,3)
result = sum(*num)
print(f'sum of numbers is: {result}')