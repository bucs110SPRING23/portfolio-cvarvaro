import random

# Functions should have on responsibility
# Avoid making functions responsible for input 

# def foo(x, y, z):
#     print(x, y, z)

# foo(1,2,3)
# foo(2,1,3)
# #foo(3, 2) # ERROR - Not enough parameters 

# def bar(x=0,y=2,z=3):
#     print(x, y, z) 

# bar(1,2)

# global_var = 5
# def foo():
#     local_var = 5 # local sope

# Local variables get deleted at the end of the function
# Parameters are local variables

# return None: NoneType

# def bar():
#     x = 5
#     return x, 6

# y = bar()
# print(y)

# name collisions 
# global variables never leave memory while the program is running

# def percentage_to_letter(percent):
#     let = "A"
#     if 80 <= percent < 90:
#         let = "B"
#     elif 70 <= percent < 80:
#         let = "C"
#     elif 60 <= percent < 70:
#         let = "D"
#     elif percent < 60:
#         let = "F"
#     return let

# def is_passing(letter):
#     return letter.lower() in "abc"

# def main():
#     grades = [90, 80, 70, 60, 50]
#     for grade in grades:
#         letter = percentage_to_letter(grade)
#         if is_passing(letter):
#             print("you passed!")
#         else:
#             print("Someone messed up your grades")

# main()

def remove_vowels(string):
    vowels = "aeiou"
    vowels += vowels.upper()
    result = ""
    for ch in string:
        if ch not in vowels:
            result += ch
    return result

def main():
    mystring = "Hello World!"
    mystring = remove_vowels(mystring)
    print(mystring)


main()