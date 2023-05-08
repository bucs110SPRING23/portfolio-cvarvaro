import json

def main():
    news = "news.txt"
    json = "susb.json"
    fptr = open(news, "r")
    fptr2 = open(json, "r")
    accumulator = 0
    for ch in fptr.read():
        if ch.isalnum():
            accumulator += 1
    fptr.close()
    
    fptr = open("news.txt", "w")
    data = str(accumulator) + "something"
    fptr.write()


