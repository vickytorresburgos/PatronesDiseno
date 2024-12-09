import logging

class Logger:
    _instance = None # garantiza que solo haya una instancia

    def __new__(cls, *args, **kwargs): # asegura que solo se cree una instancia de la clase Logger
        if not cls._instance: # si no hay ninguna instancia almacenada en _instancia (es decir, si es None), entonces crea una nueva instancia.
            cls._instance = super().__new__(cls, *args, **kwargs)
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
            cls._logger = logging.getLogger()
        return cls._instance

    def log(self, message):     
        self._logger.info(message)

logger1 = Logger()
logger1.log("Primer mensaje del log")

logger2 = Logger()
logger2.log("Segundo mensaje del log")

print(logger1 is logger2)