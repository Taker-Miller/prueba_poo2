from Empleado import Empleado
from Gerente import Gerente

while True:
    print("menu")
    print("1- empleado")
    print("2- gerente")
    print("3- salir")
    opcion = input("ingresa una opcion: ")

    if opcion == "1":
        nombre = input("ingresa nombre empleado: ")
        while True:
            try:
                hrs_trabajadas = int(input("ingresa hrs trabajadas: "))
                if hrs_trabajadas > 0:  
                    break
                else:
                    print("Las horas trabajadas deben ser mayores a 0.")
            except:
                print("debes ingresar valores numericos")
                
        while True:
            try:
                salario_por_hr = int(input("ingresa salario por hr: "))
                if salario_por_hr > 0:  
                    break
                else:
                    print("El salario por hora debe ser mayor a 0.")
            except:
                print("debes ingresar valores numericos")
                
        e = Empleado(nombre, hrs_trabajadas, salario_por_hr)
        e.ver_informacion()

    elif opcion == "2":
        nombre = input("ingresa nombre del gerente: ")
        while True:
            try:
                hrs_trabajadas = int(input("ingresa hrs trabajadas: "))
                if hrs_trabajadas > 0: 
                    break
                else:
                    print("Las horas trabajadas deben ser mayores a 0.")
            except:
                print("debes ingresar valores numericos")
                
        while True:
            try:
                salario_por_hr = int(input("ingresa salario por hr: "))
                if salario_por_hr > 0: 
                    break
                else:
                    print("El salario por hora debe ser mayor a 0.")
            except:
                print("debes ingresar valores numericos")
                
        tiene_bono = input("tiene bono? (s/n): ").lower()
        bono = 0  
        if tiene_bono == 's':
            while True:
                try:
                    bono = int(input("ingresa bono: "))
                    if bono > 0: 
                        break
                    else:
                        print("El bono debe ser mayor a 0.")
                except:
                    print("debes ingresar valores numericos")
                    
        g = Gerente(nombre, hrs_trabajadas, salario_por_hr, bono)
        g.ver_informacion()

    elif opcion == "3":
        print("Hasta Luego")
        break

    else:
        print("ingresa una opción del 1 al 3")
