import json
import random
import os
def main():
    json_data = json.load(open("assets/ideas.txt", "r"))
    print(random.choice(json_data))
main()