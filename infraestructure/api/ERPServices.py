import requests
from utils.singleton import singleton

@singleton
class ERPServices:
    def __init__(self):
        """
        Constructor de la clase ProductsServices.
        Esta clase se encarga de interactuar con la API de productos.
        """
        pass    
    
    def obtain_products(self):
        """
        This function obtains the list of products from the API and returns it as a JSON object.
        """
        # Send a GET request to the API endpoint
        response = requests.get(
            "https://crmniv.azurewebsites.net/api/Products", timeout=400)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response into a Python object
            data = response.json()
            return data
        else:
            # If the request failed, return an empty list
            return []


