def reverse(n, rev=0):
    if n == 0:
        return rev
    return reverse(n//10, rev*10 + n%10)

num = int(input("Enter number: "))

if num == reverse(num):
    print("Palindrome")
else:
    print("Not Palindrome")
