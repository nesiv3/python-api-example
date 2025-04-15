import requests
from config.settings import API_BASE_URL
from utils.singleton import singleton

@singleton
class ERPServices:
    def __init__(self):
        """
        Constructor de la clase ERPServices.
        Esta clase se encarga de interactuar con la API de productos.
        Actualmente no realiza ninguna acción específica, pero está preparada
        para inicializar configuraciones futuras si es necesario.
        """
        pass    
    
    def obtain_products(self):
        """
        Este método obtiene la lista de productos desde la API y la devuelve como un objeto JSON.

        Pasos:
        1. Envía una solicitud GET al endpoint de la API para obtener los productos.
        2. Verifica si la solicitud fue exitosa (código de estado 200).
        3. Si la solicitud es exitosa, convierte la respuesta JSON en un objeto de Python y lo devuelve.
        4. Si la solicitud falla, devuelve una lista vacía como valor predeterminado.

        Returns:
            list: Lista de productos obtenidos de la API o una lista vacía si la solicitud falla.
        """
        # Envía una solicitud GET al endpoint de la API
        response = requests.get(
           API_BASE_URL + "/Products", timeout=400)

        # Verifica si la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            # Convierte la respuesta JSON en un objeto de Python
            data = response.json()
            return data
        
        # Si la solicitud falla, devuelve una lista vacía
        return []


