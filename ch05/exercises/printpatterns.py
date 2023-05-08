num_stars = int(input("How many layers is the pyramid: "))

def star_pyramid():
    for i in range(1, num_stars + 1):
        print("*" * i)

star_pyramid()