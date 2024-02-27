#addition of all the digits in the number

num = int(input('enter the number \n'))
numtotal = 0
while num !=0:
    digit = num % 10
    numtotal = numtotal+digit
    num //=10 #(this is similar as num = int(num/10), to use the result in int form we are using //

print(numtotal)

