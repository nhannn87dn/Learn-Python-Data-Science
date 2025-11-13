myTuple = ("apple", "banana", "kiwi", "melon")
print(type(myTuple))

# (a, b, k) = myTuple
# print(b)
(_, b, *r) = myTuple
print(r)



# m = ("apple",)
# print(type(m))

# myList = list(myTuple)
# myList[0] = 'melon'
# myTuple = tuple(myList)
# print(myTuple)