# checking the datatypes of the list

# ff = [1,2,3,'ddd']
# print(type(ff)) #<class 'list'>

# checking the list is empty or not
# dd = [1]
#
# if not dd:
#     print('empty')
# else:
#     print('not empty')

# example 3

# ww = 'Dhruv Raiyani'
# wwlistus = list(ww)
# wwlist = sorted(list(ww))
#
# print(wwlistus)
# print(wwlist)

#tuples

#example 4
# checking the tuple is empty or not
# mytuple1 = ()
# if not mytuple1:
#     print('empty')
# else:
#     print('not empty')


#example 5

# astr = 'Raiyani'
# mytuple2 = tuple(astr)
# print(mytuple2)
#
# print(mytuple2[4])
# print(mytuple2[::-1])

#example 6
#merging tuples

# mytuple3 = ('dhruv', 'raiyani')
# mytuple4 = ('dhruv', 'patel')
#
# MyTupleMerge = mytuple4+mytuple3
# print(MyTupleMerge)


#example 7
#tuple assign to multiple values

# a,b,c = (1,2,3)
# print(a)
# print(b)
# print(c)
#
# d,e,f = ('dhruv', 'patel', 'raiyani')
# print(d)
# print(e)
# print(f)


#example 8
#nested tuples

# mytuple5 = ('gujarat', 'mp')
# mytuple6 = ('rajasthan', 'delhi')
#
# mytuple7 = ('indian states', mytuple6, mytuple5)
# print(mytuple7)
#
# print(mytuple7[0])
# print(mytuple7[1])
# print(mytuple7[2])
# print(mytuple7[1][0])
# print(mytuple7[2][1])


#example 9
#search in tuple

mytuple8 = ('toronto', 'ohio', 'chicago', 'new york')
print(mytuple8)
print('new york' in mytuple8)
print('delhi' in mytuple8)


