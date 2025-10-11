from abc import ABC, abstractmethod

# Interfaces 
class IEnviarMensaje(ABC):
    @abstractmethod
    def enviar_mensaje(self, usuario_emisor, usuario_receptor, asunto, cuerpo):
        pass

class IRecibirMensaje(ABC):
    @abstractmethod
    def ver_entradas(self):
        pass

class IListarMensajes(ABC):
    @abstractmethod
    def ver_enviados(self):
        pass
