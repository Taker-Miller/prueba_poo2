from Estudiante import Estudiante
from Escuela import Escuela

escuela = Escuela()
for i in range(3): 
    nombre = input("ingresa el nombre del estudiante: ")
    while True:
        try:
            edad = int(input("ingresa la edad del estudiante: "))
            if edad >= 5:
                break
            else:
                print("La edad debe ser mayor o igual a 5")
        except:
            print("ingresa un valor numerico.")
    
    notas = []
    for n in range(2):
        while True:
            try:
                nota = float(input(f"ingresa la nota {n+1} del estudiante: "))
                if 1.0 <= nota <= 7.0:
                    notas.append(nota)
                    break
                else:
                    print("La nota debe estar entre 1.0 y 7.0.")  
            except: 
                print("ingresa una nota válida.")
    
    estudiante = Estudiante(nombre, edad, notas)
    escuela.agregar_estudiante(estudiante)

print("ESTUDIANTES:")   
escuela.listar_estudiantes()