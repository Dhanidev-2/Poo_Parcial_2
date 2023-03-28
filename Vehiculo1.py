from dataclasses import dataclass

@dataclass
class Vehiculo:
    marca: str
    modelo: str
    añoFabricacion: int
    _velocidadMaxima: float
    velocidadInicial:float = 0.00

    def acelerar(self, segundos: int|float) -> int|float:
        aceleracionConstante = 9.8 #m/s^2

        self.velocidadInicial = self.velocidadInicial + segundos*aceleracionConstante
        return self.velocidadInicial 
    
    def frenar(self, segundos: int|float) -> int|float:
        desaceleracionConstante = 9.8 #m/s^2
        self.velocidadInicial = self.velocidadInicial - (segundos*desaceleracionConstante)
        return self.velocidadInicial

    def mostrar_datos(self):
        return f'Marca del vehiculo {self.marca} modelo {self.modelo} año fabricación {self.añoFabricacion} velociada máxima {self._velocidadMaxima} velocidad inicial {self.velocidadInicial}'

