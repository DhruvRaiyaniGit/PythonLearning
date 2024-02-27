# Note - there are multiple programs in the single python file, each program are individual and doesnt correlate with each other, threfore running the single program, make other program as a comment


#Program-1

#check the given string is palindrom or not

#by tradiational method
#
# def reverse_string(input_str):
#     rev_str=''
#     for c in input_str:
#         rev_str = c+rev_str
#     return rev_str
#
# original_string = input('enter your string to check the palindrom \n')
#
# reversestring = reverse_string(original_string)
# print(reversestring)
#
# print(f'{original_string} the string is palindrom' if original_string==reversestring else f'{original_string} is not palindrom')


#Program-2
#reverse string function practice
'''giving argument through defined variable. we need to assign arg everytime when we call the function
by passing args we are resuing the same function multiple times, in the next program we are not using args while defining the function'''


# def rs(inpstr):
#     rev=''
#     for char in inpstr:
#         rev = char+rev
#     return rev
#
# originalstr='dhruv'
# revresult = rs(originalstr)
# print(f'Reverse result is {revresult}')
# print(f'{originalstr} is palindrome' if revresult==originalstr else f'{originalstr} is not palindrome')


#Program-3
#reverse string function practice

# inpstr = input('enter the palindrome string to validate \n')
# def rs():
#     rev=''
#     for char in inpstr:
#         rev = char+rev
#     return rev
#
# revresult = rs()
# print(f'Reverse result is {revresult}')
# print(f'{inpstr} is palindrome' if revresult==inpstr else f'{inpstr} is not palindrome')



#program - 4
#reverse string using the slicing function
#calling a function will directly print the result


# inpstr = input('enter the string to check for palindrome \n')
#
# def palindromecheck():
#     rev = inpstr[::-1]
#     if rev == inpstr:
#         print('your string is palindrome')
#     else:
#         print('your string is not palindrome')
#
# palindromecheck() #this is calling the function


#program - 5
#reversing a string using a for loop
#
# ccc= ''
# for i in 'dhruv':
#     ccc=i+ccc
#
# print(ccc)


#program -6
#using join and reversed function
# inpstr = input('enter the string to check for palindrome \n')
# def reversestr(inpstr):
#     return ''.join(reversed(inpstr))
#
# revvv = reversestr(inpstr)
# print(revvv)


#program - 7
#using join and reversed function
inpstr = input('enter the string to check for palindrome \n')

def reversestr():
    revs = ''.join(reversed(inpstr))
    if revs == inpstr:
        print('palindrome')
    else:
        print('not a palindrome')

reversestr()