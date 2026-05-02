def count_digits(n):
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count

num = int(input("Enter number: "))
print("Digits:", count_digits(num))
