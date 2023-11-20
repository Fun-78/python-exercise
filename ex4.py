# while loop is uesd to keep asking the input untilla valid num has been entererd
while True:
    num = int(input('enter a num in the range 1-10: '))
    if 1 <= num <= 10:
        break
    else:
        print("try again")
print(f'number is: {num}')

