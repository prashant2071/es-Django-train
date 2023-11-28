# tuple is ordered and cannot be changable
animal =("elephant","dog","cat","lion")
# tuple can be change into list
arrays=list(animal)
# after changing into list it can be removed
arrays.remove("elephant")
animal= tuple(arrays)
print(animal)
print(arrays)

# destructing tuples .aka unpacking 
fruits1=("apple", "banana", "cherry")
(green1, yellow1, red1) = fruits1

print(green1)
print(yellow1)
print(red1)
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# asteriks refers to as rest operator in javascript
(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

