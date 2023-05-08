# Network programming

# Build a program that asks trivia questions

# Server: Any computer listening for any incoming network connections

# Request: An incoming connection that asks for some resource from the server

# - Images, video, music
# - Text
# - JSON
# - HTML

# - Types of requests

# - GET - Read operation
# visiting, downloading a file, etc

# - PUT - Write operation (requires security)
# login, deleting, 

# Headers
# - Sent with request and the response

# - Status codes
#       - 200: ok, everything went fine
#       - 400: resource cannot be delivered
#       - 500: bad code server

# - IP Address
# - System information (geolocation)

## urllib

# Requests

# API - Application Programmer's interface
# APIs can return data in any format,
# usually returned in JSON

# URL Parameters

# ?, &

# binghamton.edu/cs?

import requests
import random

# def main():
#     response = requests.get("http://icanhazip.com")
#     print(response.status_code)
#     print(response.headers)
#     print(response.text)

class TriviaProxyAPI:
    def __init__(self):
        self.url = "https://opentdb.com/api.php?"
        self.varstr = "amount=2&category=18"
    
    def get(self):
        url = self.url + self.varstr
        response = requests.get(url)
        data = response.json()
        return data['results']

def main():
    response = requests.get("https://opentdb.com/api.php?amount=10")
    data = response.json()
    print(data)
    results = data['results']
    for r in results:
        print(r('question'))
        possibles = [r["correct_answer"]] + r["incorrect_answers"]
        random.shuffle(possibles)
        print("Make your selection: ")
        for i, p in enumerate(possibles):
            print(f"{i}) {p}")

main()


