from Circulo import Circulo
while True:
    try:
        radio = float(input("Ingresa radio: "))
        c = Circulo(radio)
        c.imprimir_resultados()
        break
    except:
        print("valor invalido, ingresa un valor numerico (si es decimal se añade punto)")
while True:
    opcion = input("¿Quieres cambiar el radio? (s/n): ")
    if opcion.lower() == "s":
        while True:
            try:
                nuevo_radio = float(input("Ingresa nuevo radio: "))
                break
            except:
                print("valor invalido, ingresa un valor numerico (si es decimal se añade punto)")
        c.cambiar_radio(nuevo_radio)
        c.imprimir_resultados()
        
    elif opcion.lower() == "n":
        print("Hasta Luego")
        break
    else:
        print("opción no válida.")