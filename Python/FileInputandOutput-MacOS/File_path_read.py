import os

# Use Mac OS style file path
file_path = "/Users/heinrich-mac16/Desktop/GitHubCode/Python/FileInputandOutput/checkfile.txt"

if not os.path.isfile(file_path):
    print(f"The file at '{file_path}' does not exist.")
else:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
