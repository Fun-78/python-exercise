thing = []
thing2 = [0.0] *5
print(f'thing: {thing}')
print(f'thing2: {thing2}')
print('intergers from 0 to 3: ')
for i in range(4):
    print(i)
print('intergers from 4 to 7: ')
for i in range(4,8):
    print(i)
print('intergers from 2 to 8: ')
for i in range(2,9,2):
    print(i)

thing = list(range(6))
print(f'is 3 in thing: {"yes" if 3 in thing else "no"}')
print(f'is 6 in thing: {"yes" if 6 in thing else "no"}')

