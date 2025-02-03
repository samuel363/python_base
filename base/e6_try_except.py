""" Excepcion personalizada """
class MyCustomError(Exception):
    pass

""" Ejemplo de Try Except """
try:
    numerator = int(input("Introduce el numerador: "))
    denominator = int(input("Introduce el denominador: "))

    if numerator == 0:
        raise MyCustomError("Se produjo un error personalizado")

    result = numerator / denominator
    print(f"OK: El resultado de la división es: {result}")

except ZeroDivisionError:
    print("Error: No puedes dividir por cero.")
except ValueError:
    print("Error: Entrada no válida. Por favor, introduce un número entero.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {str(e)}")
finally:
    print(f"Esto siempre cierra aca..")