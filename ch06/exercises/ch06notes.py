import json

# # Files
# # - Saved program state

# # Operating System: - manages files
# # Request the file from OS
# # - Where
# # - Name
# # - How to use it

# # - Working eith files is one-way 

# def main():
#     # file_pointer = open("ideas.txt", "r") # FILE TYPE
#     # ideas = file_pointer.readline()
#     # # idea = input("Enter an idea: ")
#     # # ideas = []
#     # # ideas.append(idea)
#     # print(ideas)
#     # ideas = file_pointer.readline()
#     # print(ideas)
#     # file_pointer.close()
#     file_pointer = open("ideas.txt", "a")

#     # Modes: 'r', 'w', 'a'
#     file_contents = file_pointer.read() # Entire files in a single string
  

#     idea = input("Enter Idea: ")
#     ideas = []
#     ideas.append(idea)
    
#     for i in ideas:
#         file_pointer.write(i) 
# main()


# File streams - one way
# 'w' - deletes any existing file, truncate the file

# def main():
#     filename = "ideas.txt"
#     fptr = open(filename, "r")
#     accumulator = 0
#     for ch in fptr.read():
#         if ch.isalnum():
#             accumulator += 1
#     fptr.close()

#     fptr = open(filename+".dat", "w")
#     data = str(accumulator) + "characters" # f"{accumulator} characters
#     fptr.write(data)
#     fptr.close() 

# main()

