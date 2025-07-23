import os
# Use raw string for file path or ask user for input
file_path = r"C:\Users\Dell User\Desktop\GitHubCode\Python\FileInputandOutput\checkfile.txt"
# file_path = input("Enter the full file path: ")

if not os.path.isfile(file_path):
    print(f"The file at '{file_path}' does not exist.")
else:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)
    except IOError:
        print(f"An error occurred while reading the file at '{file_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
