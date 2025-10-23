try: # Es ideal ubicar en el try únicamente las operaciones con mayor posibilidad de error.
    entero = int(input("Ingrese un número: "))
except ValueError:
    print("El valor ingresado no es válido")
else: 
    print("Gracias por utilizar el programa")
finally:

    try:
        print(f"El número ingresado es: {entero}")
    except:
        print("-- HA OCURRIDO UN ERROR: EL NÚMERO NO PUEDE IMPRIMIRSE--")
    print("Programa concluido.")

