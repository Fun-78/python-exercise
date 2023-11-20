A = 2026
if (A % 4 == 0 and A % 100 != 0) or (A % 400 == 0):
    print(A,'is a leap year')
else:
    print(A,'is not a leap year')