class Circulo:
    def __init__(self, radio):
        self.radio = radio  

    def calcular_area(self):
        return 3.14 * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * 3.14 * self.radio

    def cambiar_radio(self, nuevo_radio):  
        self.radio = nuevo_radio

    def imprimir_resultados(self):
        print(f"Radio: {self.radio}")
        print(f"Área: {self.calcular_area()}")
        print(f"Perímetro: {self.calcular_perimetro()}")
