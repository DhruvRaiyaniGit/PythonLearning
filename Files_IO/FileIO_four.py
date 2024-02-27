# File handlind - how to read and write using the python code

#open a file
# file_obj = open('filename', mode)

#Modes
""" 'r' for reading (default)
'w' for writing
'a' for appending
'b' for binary mode
'+' for updating (reading and writing)
"""

# Read a file
"""
for reading entire content: content = file_object.open()
line: file_object.readline()
lines: file_object.readlines()
"""

# erite to a file
"""
writing string = file_object.write()
writing multiple lines = file_object.writelines()
"""

#closing a file
# file_object.close()

try:
    with open('text_file_one.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError as error:
    print(error)



