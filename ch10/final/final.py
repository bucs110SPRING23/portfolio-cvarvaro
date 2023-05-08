import requests
import json
from randomjoke import RandomJokeAPI
from randomdog import RandomDogAPI

def main():
    RandomJokeAPI.random_joke()
    RandomDogAPI.random_dog_image()

main()