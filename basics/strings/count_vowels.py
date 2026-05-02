s = input("Enter string: ")
vowels = "aeiouAEIOU"
count = 0

for i in s:
    if i in vowels:
        count += 1

print("Vowels =", count)
