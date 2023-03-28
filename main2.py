from alumnos import *

def main():

    alumno1 = Alumno("Dani", 18, [1.0, 2.0, 5.0])
    print(alumno1.promedio())
    print(alumno1.nota_mayor())
    print(alumno1.nota_menor())
    """alumno2 = Alumno("Ela", 17, [1.0, 3.0, 5.0])
    alumno3 = Alumno("Isa", 17, [1.0, 4.0, 5.0])
    alumno4 = Alumno("Salo", 17, [5.0, 4.0, 5.0])"""

    lista = {"alum1": ["Dani", 18, [1.0, 2.0, 5.0]],
             "alum2": ["Ela", 17, [1.0, 3.0, 5.0]],
             "alum3": ["Isa", 17, [1.0, 4.0, 5.0]],
             "alum4": ["Salo", 17, [5.0, 4.0, 5.0]]}

    imprimir = lista
    print(imprimir)

if __name__ == "__main__":
    main()