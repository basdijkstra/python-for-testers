# Exercise 6.1
# Create a method write_and_read_file() that does the following:
# Create a new file file.txt (Python will create a file that you
# try to open a file that doesn't exist) with "write" privileges.
# Write three random lines to the file and close it.
# Reopen the file and print its contents.

def write_and_read_file():
    file = open("file.txt", "w")
    file.write("Line 1\n")
    file.write("Line 2\n")
    file.write("Line 3")
    file.close()

    file = open("file.txt")
    print(file.read())
    file.close()

write_and_read_file()

# Exercise 6.2
# Create a method append_to_file() that reopens the file you
# created in the previous exercise and appends two more lines
# to it. Print the contents to the console output once again
# to check whether or not it is working. Think about placing
# line breaks properly to make your file humanly readable!

def append_to_file():
    file = open("file.txt", "a")
    file.write("\nLine 4")
    file.write("\nLine 5")
    file.close()

    file = open("file.txt")
    print(file.read())
    file.close()

append_to_file()