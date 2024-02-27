#reading the file

file = open('file_one', 'r')
print(file.read())
file.close()

file2 = open('text_file_one.txt', 'r')
print(file2.read())
file2.close()


# Append in file

file3 = open('text_file_one.txt', 'a')
file3.write("Shri Hari | Shri Hari | Shri Hari")
file3.close()


# writing in file

file4 = open('text_file_one2.txt', 'w')
file4.write('Sita Ram | Sita Ram')
file4.close()

file5 = open('text_file_one2.txt', 'r')
print(file5.read())