import os

# Expand ~ to the full home directory path
file_path = os.path.expanduser("~/Desktop/GitHubCode/Python/FileInputandOutput-MacOS/checkfile.txt")

# Create the file if it doesn't exist
if not os.path.isfile(file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write("This is a new file.\nYou can add your content here.")

# Now read and print the file content
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)
except Exception as e:
    print(f"An error occurred while reading the file: {e}")
