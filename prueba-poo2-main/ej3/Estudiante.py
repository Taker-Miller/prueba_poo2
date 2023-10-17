class Estudiante:
    def __init__(self, nombre, edad, notas):
        self.__nombre = nombre
        self.__edad = edad
        self.__notas = notas

    def get_nombre(self):
        return self.__nombre #devuelve el valor actual del atributo nombre.

    def set_nombre(self, nombre): #permite cambiar el valor del atributo nombre
        self.__nombre = nombre

    def get_edad(self): 
        return self.__edad #devuelve el valor actual del atributo edad.

    def set_edad(self, edad): #permite cambiar el valor del atributo edad
        self.__edad = edad

    def get_promedio(self):
        return sum(self.__notas) / len(self.__notas) #obtiene el promedio mediante la suma de las notas y luego se divide por la cantidad de notas

    def agregar_nota(self, nota):
        self.__notas.append(nota)
        #agrega notas a la lista de notas de la instancia de la clase en la que se utiliza.
