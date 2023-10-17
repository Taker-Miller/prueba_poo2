class Empleado:
    def __init__(self, nombre, hrs_trabajadas, salario_por_hr):
        self.__nombre = nombre
        self.__hrs_trabajadas = hrs_trabajadas
        self.__salario_por_hr = salario_por_hr

    def get_nombre(self):
        return self.__nombre #devuelve el valor actual del atributo nombre.
    def set_nombre(self, nombre): #permite cambiar el valor del atributo nombre
        self.__nombre = nombre

    def get_hrs_trabajadas(self):
        return self.__hrs_trabajadas  #devuelve el valor actual del atributo hrs_trabajadas.
    def set_hrs_trabajadas(self, hrs_trabajadas): #permite cambiar el valor del atributo hrs_trabajadas
        self.__hrs_trabajadas = hrs_trabajadas

    def get_salario_por_hr(self):
        return self.__salario_por_hr  #devuelve el valor actual del atributo salario_por_hr.
    def set_salario_por_hr(self, salario_por_hr): #permite cambiar el valor del atributo salario_por_hr
        self.__salario_por_hr = salario_por_hr

    def calcular_salario(self):
        return self.__salario_por_hr * self.__hrs_trabajadas #calcula el salario multiplicando salario por hr por hrs trabajadas

    def ver_informacion(self):
        print(f"Nombre: {self.get_nombre()}")
        print(f"Horas trabajadas: {self.get_hrs_trabajadas()}")
        print(f"Salario por hora: {self.get_salario_por_hr()}")
        print(f"Salario total: {self.calcular_salario()}")
        #muestra la informacion del empleado

