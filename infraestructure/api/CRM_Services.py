from utils.singleton import singleton


@singleton
class CRM_Services:
    def __init__(self):
        """
        Constructor de la clase CRM_Services.
        Esta clase se encarga de interactuar con la API de productos.
        """


    def obtain_user_by_id(self, user_id):
        """
        This function obtains user information by ID from the API.

        Args:
            user_id (int): The ID of the user to retrieve

        Returns:
            dict: User information including name, last name, email, address and user type
        """
        # En un entorno real, enviarías una solicitud GET a la API con el ID del usuario
        # response = requests.get(f"https://crmniv.azurewebsites.net/api/Users/{user_id}", timeout=400)

        # Por ahora, simularemos la respuesta con datos de ejemplo
        # Esta sería la estructura de la respuesta que esperarías de tu API

        # Check if the request was successful (status code 200)
        try:
            # Datos simulados para demostración
            sample_user_data = {
                "id": user_id,
                "nombre": "Juan Carlos",
                "apellido": "Rodríguez Gómez",
                "email": "jcrodriguez@ejemplo.com",
                "direccion": "Calle Principal 123, Ciudad de México",
                "tipo_usuario": "PREMIUM"
            }

            return sample_user_data
        except Exception as e:
            print(f"Error al obtener datos del usuario: {str(e)}")
            return {
                "error": "No se pudo obtener la información del usuario",
                "mensaje": str(e)
            }
