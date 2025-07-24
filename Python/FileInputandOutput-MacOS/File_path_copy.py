import os
import shutil

# Set different source and destination paths
source_path = os.path.expanduser("~/Desktop/GitHubCode/Python/FileInputandOutput-MacOS/checkfile.txt")
destination_path = os.path.expanduser("~/Desktop/GitHubCode/Python/FileInputandOutput-MacOS/checkfile-CopyMacOS.txt")
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