from Empleado import Empleado
class Gerente(Empleado):
    def __init__(self, nombre, hrs_trabajadas, salario_por_hr, bono):
        super().__init__(nombre, hrs_trabajadas, salario_por_hr)
        self.__bono = bono

    def get_bono(self):
        return self.__bono
    def set_bono(self, bono):
        self.__bono = bono

    def calcular_salario(self):
        return super().calcular_salario() + self.__bono

    def ver_informacion(self):
        print(f"Nombre: {self.get_nombre()}")
        print(f"Horas trabajadas: {self.get_hrs_trabajadas()}")
        print(f"Salario por hora: {self.get_salario_por_hr()}")
        print(f"Bono: {self.get_bono()}")
        print(f"Salario total: {self.calcular_salario()}")



       
