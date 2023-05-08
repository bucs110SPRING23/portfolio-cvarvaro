import requests
import json

class RandomJokeAPI:
    def __init__(self):
        self.joke_url = "https://official-joke-api.appspot.com/random_joke" 

    def random_joke():
        response = requests.get(RandomJokeAPI().joke_url)
        data = response.json()

        if "setup" in data and "punchline" in data:
            setup = data["setup"]
            punchline = data["punchline"]
            print("Joke:")
            print(setup)
            print(punchline)
        else:
            print("No joke found.")


class RandomDogAPI:
    def __init__(self):
        self.dog_url = "https://random.dog/woof.json" 
        
    def random_dog_image():
        response = requests.get(RandomDogAPI().dog_url)
        data = response.json()
        
        if "url" in data:
            dog_image_url = data["url"]
            print("Dog Image:", dog_image_url)
        else:
            print("No dog image found.")

def main():

    RandomJokeAPI.random_joke()
    RandomDogAPI.random_dog_image()

main()