# Exceptions
# An exception is an event that occurs during the execution of the program
# That disrupts the normal flow of exceptions

A = int(input("Enter the value of A "))
B = int(input("Enter the Value of B "))

try:
    c = A / B
    print(c)
except Exception as error:
    print("You are dividing with 0, please enter the number greater than 0")

