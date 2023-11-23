# Import the module os that provides tools to work with the operating system of your computer.
import os

file_name = input("Please write the name of the file to work with:\n")

if os.path.exists(file_name):
    # Open the file in the reading mode, read its content.
    with open(file_name) as file:
        content = file.read()
    # Apply the previously defined function process() to the text taken from the file.
    new_content = process(content)

    with open(f'{file_name}_processed.txt', 'w') as new_file:
        new_file.write(new_content)

    print("All done!")

else:
    print("The file you entered does not exist!")
