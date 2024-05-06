#Program to Create a file, Write in to file, read a file' append the file

# Function to create a file and write to it
def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

# Function to read from a file
def read_from_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
        print("Content of the file:")
        print(content)

# Function to append to a file
def append_to_file(filename, content):
    with open(filename, 'a') as file:
        file.write("\n" + content)

# Create a file and write to it
filename = "example.txt"
write_to_file(filename, "Hello, this is a test file.")

# Read from the file
read_from_file(filename)

# Append to the file
append_to_file(filename, "Appending some more content.")

# Read from the file after appending
read_from_file(filename)
