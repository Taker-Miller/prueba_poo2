class Estudiante:
    def __init__(self, nombre, edad, notas):
        self.__nombre = nombre
        self.__edad = edad
        self.__notas = notas

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad

    def get_promedio(self):
        return sum(self.__notas) / len(self.__notas)

    def agregar_nota(self, nota):
        self.__notas.append(nota)