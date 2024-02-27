#dictionary

#example 1
#creating empty dict
myset1 = {}
print(myset1)
print(type(myset1))  #<class 'dict'>


#example 2

#create a dict using an user imput

mydict1={}

key = input('enter the key')
value = input('enter the value')

mydict1[key] = value

print(mydict1)

print(mydict1.items())
print(mydict1.keys())
print(mydict1.values())


