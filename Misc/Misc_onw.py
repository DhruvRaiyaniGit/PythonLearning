# Anagram string

String1 = input("Enter your first input ")
String2 = input("Enter your second string ")

String1ToList = list(String1)
String2ToList = list(String2)

if list.sort(String1ToList) == list.sort(String2ToList):
    print("Strings are Anagram")
else:
    print("Strings are NOT Anagram")
