# using else in the try block

try:
    fileread = open('text_file_one.txt', 'r')
    contents = fileread.read()
    print(contents)

except FileNotFoundError:
    print('File not found')

except IOError:
    print('An error occurred while reading the file')

else:
    print("File reading completed successfully.")