def frequency(s):
    words = s.lower().split()
    
    word_freq = {}
    
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    
    return dict(sorted(word_freq.items()))

input_string = input("ENTER A STRING : ")
result = frequency(input_string)

for word, freq in result.items():
    print(f"{word} : {freq}")
