import os
# Use raw string for file path or ask user for input
file_path = os.path.expanduser("~/Desktop/GitHubCode/Python/FileInputandOutput-MacOS/checkfile-CopyMacOS.txt")
# file_path = input("Enter the full file path: ")

if not os.path.isfile(file_path):
    print(f"The file at '{file_path}' does not exist.")
else:
    try:
        os.remove(file_path)
        print(f"The file at '{file_path}' has been removed.")
    except IOError:
        print(f"An error occurred while removing the file at '{file_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")