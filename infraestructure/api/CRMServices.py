from utils.singleton import singleton


@singleton
class CrmServices:
    def __init__(self):
        """
        Constructor de la clase CrmServices.
        Esta clase se encarga de interactuar con la API de usuarios.
        Actualmente no realiza ninguna acción específica, pero está preparada
        para inicializar configuraciones futuras si es necesario.
        """

    def obtain_user_by_id(self, user_id):
        """
        Este método obtiene la información de un usuario desde la API utilizando su ID.

        Pasos:
        1. En un entorno real, se enviaría una solicitud GET al endpoint de la API con el ID del usuario.
        2. Por ahora, se simula la respuesta con datos de ejemplo.
        3. Si ocurre un error, se maneja adecuadamente y se devuelve un mensaje de error.

        Args:
            user_id (int): El ID del usuario que se desea obtener.

        Returns:
            dict: Un diccionario con la información del usuario, incluyendo:
                  - id: ID del usuario.
                  - nombre: Nombre del usuario.
                  - apellido: Apellido del usuario.
                  - email: Correo electrónico del usuario.
                  - direccion: Dirección del usuario.
                  - tipo_usuario: Tipo de usuario (por ejemplo, PREMIUM o BASIC).
                  Si ocurre un error, devuelve un diccionario con un mensaje de error.
        """
        # En un entorno real, enviarías una solicitud GET a la API con el ID del usuario
        # response = requests.get(f"https://crmniv.azurewebsites.net/api/Users/{user_id}", timeout=400)

        # Por ahora, simularemos la respuesta con datos de ejemplo
        # Esta sería la estructura de la respuesta que esperarías de tu API

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

        # Manejo de errores específicos
        except KeyError as e:
            # Error si falta una clave en los datos simulados
            print(f"Error: Clave no encontrada en los datos del usuario: {str(e)}")
            return {
                "error": "Clave no encontrada en los datos del usuario",
                "mensaje": str(e)
            }
        except TypeError as e:
            # Error si el tipo de dato es incorrecto
            print(f"Error: Tipo de dato incorrecto: {str(e)}")
            return {
                "error": "Tipo de dato incorrecto",
                "mensaje": str(e)
            }
        except Exception as e:
            # Error inesperado
            print(f"Error inesperado al obtener datos del usuario: {str(e)}")
            return {
                "error": "Error inesperado al obtener la información del usuario",
                "mensaje": str(e)
            }
