""" Tradicional (con valor por defecto)"""
def suma(x, y=2):
    return x + y

print(suma(1))
print(suma(1,3))
print(suma(y=1, x=3))

""" Lambda """
suma = lambda x, y=2: x + y
print(suma(1))
print(suma(1,3))


""" Con elementos variables """
# El parámetro *args recibe como una tupla un número variable de argumentos posicionales.
def suma(*args):
   resultado = 0
   # Se itera la tupla de argumentos
   for num in args:
       resultado += num #  Suma todos los argumentos
   return resultado  # Retorna el resultado de la suma
print(suma(1,2,3,4,5))


""" Con elementos clave-valor variables """
# El parámetro **kwargs recibe como un diccionario un número variable de argumentos por palabras clave.
def suma(**kwargs):
    resultado = 0
    # Se itera el diccionario de argumentos
    for key, value in kwargs.items():
        resultado += value  # Suma todos los valores de los argumentos
    return resultado

# operador de expansión **
print(suma(**{"a":1,"b":2,"c":3}))


""" Ejemplo del uso de opreador de expansion ** """
def mostrar_info(nombre, edad):
    print(f"Nombre: {nombre}, Edad: {edad}")
# Definimos un diccionario con la información
info = {"nombre": "Alice", "edad": 30}
mostrar_info(**info)

