import logging
import time

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def log_execution(func):
    """
    Decorador para registrar la ejecución de un método.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        logger.info("Ejecutando %s con argumentos %s y %s", func.__name__, args, kwargs)
        try:
            result = func(*args, **kwargs)
            elapsed_time = time.time() - start_time
            logger.info("%s ejecutado correctamente en %.2f segundos. Resultado: %s", func.__name__, elapsed_time, result)
            return result
        except Exception as e:
            logger.error("Error en %s: %s", func.__name__, str(e))
            raise
    return wrapper