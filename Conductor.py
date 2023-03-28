from dataclasses import dataclass

@dataclass
class Conductor:
    nombre: str

    def conducir_auto(self, automovil):
        automovil.acelerar(5)
        print(automovil.mostrar_datos())

    





