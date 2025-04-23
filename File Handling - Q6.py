file1 = input("Enter the first file name: ")
file2 = input("Enter the second file name: ")
output_file = input("Enter the output file name: ")

try:
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as out:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

        max_len = max(len(lines1), len(lines2))

        for i in range(max_len):
            if i < len(lines1):
                out.write(lines1[i])
            if i < len(lines2):
                out.write(lines2[i])

    print(f"Files '{file1}' and '{file2}' merged alternately into '{output_file}'.")
except FileNotFoundError:
    print("One or both input files were not found. Please check the filenames.")
