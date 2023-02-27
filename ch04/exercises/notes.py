# Iterable - you can loop over it

mystr = "hello" # iterable list of characters

mynums = [1,2,3,4,5]

for ch in mystr:
    print(ch)

for num in mynums:
    print(num)

# Anything iterable can be 'indexed into

print(mystr[0], mystr[1], mystr[2], mystr[3], mystr[4])

mynums[0] = 5
print(mynums)
mystr[0] = "j"

# Mutable = changeable
# Immutable = can't be changed once created

num = 5

mystr = "hello" # immutable
myotherstring = "hello"

mynums = [1, 2, 3, 4, 5]
myothernums = [1, 2, 3, 4, 5]

if mystr == myotherstring:
    print("same")

if mynums == myothernums:
    print("same")

if mystr is myotherstring:
    print("same")

if mynums is myothernums:
    print("same")

# Substring 
mystr = "hello"
print(mystr[0], mystr[1:4])

mystr = "j" + mystr[1:5]
print(mystr)

# Iterable objects are not always mutable

# Slicing with mutable objects 
mynums = [1,2,3,4,5]
mynums[2:2] = [2.5, 2.6]
print(mynums)

# list[index] = Value
# dictionary[key] = value
# - key/value pairs
# - keys must be unique
# - keys must be immutable