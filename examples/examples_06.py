def read_file():
    file = open("text_file.txt")
    print(file.read())
    file.close()

read_file()

def append_to_file():
    file = open("text_file.txt", "a")
    file.write("\nAdding a new line to the file..")
    file.close()

    file = open("text_file.txt")
    print(file.read())
    file.close()

append_to_file()