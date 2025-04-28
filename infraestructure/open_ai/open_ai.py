import os
from groq import Groq

from config.settings import GROQ_API_KEY

class OpenAIService:
    """
    Clase para interactuar con el servicio de Groq para generar contenido basado en IA.
    """

    def __init__(self, api_key=None):
        """
        Inicializa el cliente de Groq con la clave de API proporcionada.

        Args:
            api_key (str, optional): Clave de API para autenticar con el servicio de Groq.
                                     Si no se proporciona, se obtiene de la variable de entorno 'GROQ_API_KEY'.
        """
        self.client = Groq(api_key=api_key or os.getenv("GROQ_API_KEY", GROQ_API_KEY))

    def generar_cuerpo_correo(self, nombre_cliente):
        """
        Genera el cuerpo de un correo electrónico utilizando IA.

        Args:
            nombre_cliente (str): Nombre del cliente.
            nombre_floreria (str): Nombre de la florería.

        Returns:
            str: Contenido del correo en formato HTML.
        """
        prompt = f"""
        Escribe un correo breve y amistoso para un cliente llamado {nombre_cliente} que pidió una cotización de flores en FLORES ELEGANCIA NATURAL.
        El correo debe ser:
        - Agradecido
        - Cordial
        - Invitar a contactarse
        - Adaptarse a un tono semi-formal
        Responde solo con el cuerpo del correo en HTML.
        """

        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama-3.3-70b-versatile",
        )
        print(chat_completion)
        return chat_completion.choices[0].message.content




