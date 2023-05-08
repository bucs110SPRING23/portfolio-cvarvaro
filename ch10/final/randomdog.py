import requests
import json

class RandomDogAPI:
    """
    Fetches a random dog from Random Dog API
    """
    def __init__(self):
        """
        Initializes the class
        Sets up the URL for driver code
        """
        self.dog_url = "https://random.dog/woof.json" 
        
    def random_dog_image():
        """
        Fetches and provides a jpg for the user to view
        Prints image URL or if unable to receive, prints that no image was found
        """
        response = requests.get(RandomDogAPI().dog_url)
        data = response.json()
        
        if "url" in data:
            dog_image_url = data["url"]
            print("Dog Image:", dog_image_url)
        else:
            print("No dog image found.")