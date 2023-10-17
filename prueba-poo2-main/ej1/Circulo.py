class Circulo:
    def __init__(self, radio):
        self.__radio = radio  

    def calcular_area(self):
        return 3.14 * self.__radio ** 2
    #se toma el valor del radio almacenado en self.radio, lo eleva al cuadrado y lo multiplica por pi(3.14) para calcular y devolver el área del círculo.

    def calcular_perimetro(self):
        return 2 * 3.14 * self.__radio
    #calcula el perímetro de un círculo. multiplica dos veces pi(3.14) por el valor del radio del círculo almacenado en self.__radio y devuelve el resultado.

    def cambiar_radio(self, nuevo_radio):  
        self.__radio = nuevo_radio
    #permite cambiar el valor del radio de un círculo representado por una instancia de la clase. 
    #El nuevo valor del radio se especifica como nuevo_radio, y se asigna a self.__radio, actualizando el radio del círculo.

    def imprimir_resultados(self):
        print(f"Radio: {self.__radio}")
        print(f"Área: {self.calcular_area()}")
        print(f"Perímetro: {self.calcular_perimetro()}")
    #muestra la informacion del circulo
