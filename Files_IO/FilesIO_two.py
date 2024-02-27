# reading the file with try and except block

try:
    file1 = open('text_file_one.txt3', 'r')
    print(file1.read())
    file1.close()
except FileNotFoundError as Fnotfound:
    print("File not found", Fnotfound)