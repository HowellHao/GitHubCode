import os
import shutil

# Use raw string for file path or ask user for input
source_path = r"C:\Users\Dell User\Desktop\GitHubCode\Python\FileInputandOutput\checkfile.txt"
destination_path = r"C:\Users\Dell User\Desktop\GitHubCode\Python\FileInputandOutput\checkfile-Copy1.txt"
# source_path = input("Enter the source file path: ")
# destination_path = input("Enter the destination file path: ")

if not os.path.isfile(source_path):
    print(f"The file at '{source_path}' does not exist.")
else:
    try:
        shutil.copy(source_path, destination_path)
        print(f"The file has been copied from '{source_path}' to '{destination_path}'.")
    except IOError:
        print(f"An error occurred while copying the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")