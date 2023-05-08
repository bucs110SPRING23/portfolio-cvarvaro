def mult(x, y):
    accumulator = 0
    for i in range(y):
        accumulator += x
    return accumulator

def exp(x, y):
    accumulator = 1
    for i in range(y):
        accumulator = accumulator * x
    return accumulator

def square(x):
    return mult(x, x)

def main():
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    print(mult(x,y))
    result = exp(x, y)
    print(result)
    result = square(x)
    print(result)

main()