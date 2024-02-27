#map function usding lambda function

list1 = [1,2,3,4,5,6,7,8,9]

#storing in list
mapfun = list(map(lambda q: q**3, list1))
print(mapfun)

#storing in tuple
mapfun2 = tuple(map(lambda w: w**5, list1))
print(mapfun2)

#storing in set
mapfun3 = set(map(lambda w: w**5, list1))
print(mapfun2)

#map function using normal function/ without lambda (note: map fn is preferred to use with lambda fn)

list2 = [11,2,3,4,5,6,7,8,9]

def cubefun(x):
    return x**3

mapfun4 = list(map(cubefun, list2))


#map fn for chars

list3 = list('dhruv')
print(list3)

mapfun5 = list(map(lambda x: x*5, list3))
print(mapfun5)