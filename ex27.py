def find_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

num = int(input("Enter an integer: "))
print("The divisors of the number are:", find_divisors(num))