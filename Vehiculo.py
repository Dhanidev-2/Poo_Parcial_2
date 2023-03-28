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

        if self.velocidadInicial == segundos*aceleracionConstante:
            return self.velocidadInicial 
    
    def get_llevar(self):
        return self.velocidadInicial
    
    """def acelerar(self, segundos: int|float) -> float|int:
        aceleracionConstante = 9.8 #m/s^2
        
        if self.velocidadInicial <= self._max_speed:
            self.velocidadInicial = segundos*aceleracionConstante

        return self.velocidadInicial"""
    
    def frenar(self, segundos: int|float) -> int|float:
        desaceleracionConstante = 9.8 #m/s^2

        if self.velocidadInicial == self.velocidadInicial - (segundos*desaceleracionConstante):
            
            return self.velocidadInicial


    """def frenar(self, segundos: int|float) -> float|int:
        desaceleracionConstante = 9.8
        
        if self.velocidadInicial <= self._max_speed and self.velocidadInicial > 0:
            self.velocidadInicial = self.velocidadInicial - (segundos*desaceleracionConstante)

        return self.velocidadInicial"""

    def mostrar_datos(self):
        return f'Marca del vehiculo {self.marca} modelo {self.modelo} año fabricación {self.añoFabricacion} velociada máxima {self._velocidadMaxima} velocidad inicial {self.velocidadInicial}'

