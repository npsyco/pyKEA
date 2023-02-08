# Managing external resources to avoid memory leak

# Create a new file
# myFile = open("ExamExampleFile.txt", "x")

# Create a new file, is one doesn't exist
myFile = open("ExamExampleFile2.txt", "w")

myFile.write("Hello, World!")
myFile.close()
# This closer does not guarantee the file closing, if an exception occurs.

# We can wrap this in a 'try' 'finally' fashion

myFile = open("ExamExampleFile2.txt", "w")

try:
    myFile.write("Overwriting safely")
finally:
    myFile.close()

# Using context management protocol and the with statement, we can access the ._enter_() and ._exit_() functions:

with open("ExamExampleFile2.txt", mode="w") as file:
    file.write("More helloes!")

# Using multiple context managers:

with open('ExamExampleFile2.txt', 'r') as input_file, open('ExamExampleFile.txt', 'w') as output_file:
    content = input_file.read()
    output_file.write(content)

# Opening two files using the flags 'r' (read) and 'w' (write).
# The content of the first file is stored in the 'content' var.