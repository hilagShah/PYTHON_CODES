text = input("Enter a string: ")

char_frequency = {}

for char in text:
    char_frequency[char] = char_frequency.get(char, 0) + 1 
print("Character Frequency Dictionary:", char_frequency)
