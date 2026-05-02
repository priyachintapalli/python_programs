def reverse_num(n):
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10
    return rev

num = int(input("Enter number: "))
print("Reverse:", reverse_num(num))
