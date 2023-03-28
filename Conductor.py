from dataclasses import dataclass
from Vehiculo import get_llevar, mostrar_datos

@dataclass
class Conductor:
    nombre: str

    def conducir_auto(self):
        incremento = 5
        return self.get_llevar + incremento
    
    def get_mostrar(self):
        return mostrar_datos

    





