def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n-1)

num = int(input("Enter number: "))
print("Sum:", sum_n(num))
