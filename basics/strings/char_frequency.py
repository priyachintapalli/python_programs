def char_frequency(s):
    freq = {}

    for ch in s:
        if ch != " ":
            freq[ch] = freq.get(ch, 0) + 1

    return freq


text = input("Enter string: ")
result = char_frequency(text)

for key, value in result.items():
    print(key, ":", value)
