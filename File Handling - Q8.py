input_file = input("Enter the source file name: ")
output_file = input("Enter the output file name: ")


articles = {'a', 'an', 'the'}

try:
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            words = line.split()
            filtered_words = [word for word in words if word.lower() not in articles]
            cleaned_line = " ".join(filtered_words)
            outfile.write(cleaned_line + "\n")
    print(f"Words 'a', 'an', and 'the' removed. Output written to '{output_file}'.")
except FileNotFoundError:
    print("Input file not found. Please check the file name and try again.")
