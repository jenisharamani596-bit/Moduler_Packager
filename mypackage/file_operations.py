
# 1. Create File
def create_file():
    filename = input("Enter file name: ")
    
    with open(filename, "x") as file:
            pass
    print("File Created Successfully!")



# 2. Write to File
def write_file():
    filename = input("Enter file name: ")
    data = input("Enter data to write: ")

    with open(filename, "w") as file:
        file.write(data)

        print("Data Written Successfully!")

    

# 3. Read from File
def read_file():
    filename = input("Enter file name: ")

    
    with open(filename, "r") as file:
        data = file.read()

        print("Content:", data)
        print("Data Read Successfully!")



# 4. Append to File
def append_file():
    filename = input("Enter file name: ")
    data = input("Enter data to append: ")

    
    with open(filename, "a") as file:
        file.write(data + "\n")

        print("Data Appended Successfully!")

