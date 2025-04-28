"""
Módulo para interactuar con servicios de inteligencia artificial.
Proporciona funcionalidades para generar contenido utilizando el servicio de Groq.
"""

from .open_ai import OpenAIService

# Crear una instancia de OpenAIService para exponer el método generar_cuerpo_correo
open_ai_service = OpenAIService()

# Exponer el método generar_cuerpo_correo directamente
generar_cuerpo_correo = open_ai_service.generar_cuerpo_correo

__all__ = ["OpenAIService", "generar_cuerpo_correo"]