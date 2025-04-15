from utils.singleton import singleton


@singleton
class CrmServices:
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
                "email": "nesiv3@hotmail.com",
                "direccion": "Calle Principal 123, Ciudad de México",
                "tipo_usuario": "PREMIUM"
            }

            return sample_user_data
        except KeyError as e:
            print(f"Error: Clave no encontrada en los datos del usuario: {str(e)}")
            return {
                "error": "Clave no encontrada en los datos del usuario",
                "mensaje": str(e)
            }
        except TypeError as e:
            print(f"Error: Tipo de dato incorrecto: {str(e)}")
            return {
                "error": "Tipo de dato incorrecto",
                "mensaje": str(e)
            }
        except Exception as e:
            print(f"Error inesperado al obtener datos del usuario: {str(e)}")
            return {
                "error": "Error inesperado al obtener la información del usuario",
                "mensaje": str(e)
            }
