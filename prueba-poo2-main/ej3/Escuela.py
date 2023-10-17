from Estudiante import Estudiante
class Escuela:
    def __init__(self):
        self.__lista_estudiantes = []
    
    def agregar_estudiante(self, estudiante: Estudiante):
        self.__lista_estudiantes.append(estudiante) #permite agregar estudiantes a la lista de estudiantes de la instancia de la clase en la que se utiliza.
                
    def listar_estudiantes(self):
        for estudiante in self.__lista_estudiantes:
            print(f"Nombre: {estudiante.get_nombre()}, Edad: {estudiante.get_edad()}, Promedio: {estudiante.get_promedio()}")
    #lista y muestra información detallada de cada estudiante, incluyendo su nombre, edad y promedio
