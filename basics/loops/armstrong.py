def is_armstrong(n):
    temp = n
    sum = 0
    while n > 0:
        digit = n % 10
        sum += digit ** 3
        n //= 10
    return sum == temp

num = int(input("Enter number: "))

if is_armstrong(num):
    print("Armstrong Number")
else:
    print("Not Armstrong")
