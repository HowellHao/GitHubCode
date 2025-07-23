import os

file_path = r"C:\Users\Dell User\Desktop\GitHubCode\Python\FileInputandOutput\checkfile.txt"
content = "Hello, this is a test file.\nThis file is used for testing file reading in Python."

# Write content to file (this will create the file if it doesn't exist)
try:
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
        print(f"Content written to file at '{file_path}'.")
except IOError:
    print(f"An error occurred while writing to the file at '{file_path}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Read content from file
if not os.path.isfile(file_path):
    print(f"The file at '{file_path}' does not exist.")
else:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            print(f"Content of the file:\n{content}")
            line_count = content.count('\n') + 1
            print(f"The file contains {line_count} lines.")
            word_count = len(content.split())
            print(f"The file contains {word_count} words.")
            print(f"The file contains {len(content)} characters.")
            count_spaces = content.count(' ')
            print(f"The file contains {count_spaces} spaces.")
            count_characters_a = content.count('a')
            print(f"The file contains {count_characters_a} occurrences of the character 'a'.")
            count_characters_e = content.count('e')
            print(f"The file contains {count_characters_e} occurrences of the character 'e'.")
    except IOError:
        print(f"An error occurred while reading the file at '{file_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")