from dataclasses import dataclass
from typing import *

@dataclass
class Alumno:
    _nombre : str
    _edad: int
    _notas: List[float]

    def promedio(self):
        total = 0
        for i in range(len(self._notas)):
            total += self._notas[i]
        return total / len(self._notas)
    
    def nota_mayor(self):
        calcuMayor = max(self._notas)
        return calcuMayor
    
    def nota_menor(self):
        calcuMenor = min(self._notas)
        return calcuMenor
    
    def mejores_alumnos(self):
        mejores = []
        for i in self:
            suma=0
            