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