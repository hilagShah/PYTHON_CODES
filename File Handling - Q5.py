source_file = input("Enter the source file name: ")
target_file = input("Enter the target file name: ")

try:
    with open(source_file, 'r') as src, open(target_file, 'w') as tgt:
        for line in src:
            
            tgt.write(line.upper())
    print(f"Contents copied from '{source_file}' to '{target_file}' with uppercase conversion.")
except FileNotFoundError:
    print("Source file not found. Please check the file name and try again.")
