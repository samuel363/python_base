def mi_decorador(func):
    def wrapper():
        print("Antes de llamar a la función.")
        func()  # Llama a la función original
        print("Después de llamar a la función.")
    return wrapper

@mi_decorador
def decir_hola():
    print("¡Hola!")
decir_hola()

#Antes de llamar a la función.
#¡Hola!
#Después de llamar a la función.


def repetir(num_veces):
    def decorador(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_veces):
                func(*args, **kwargs)  # Llama a la función original
        return wrapper
    return decorador

@repetir(3)
def decir_hola(nombre):
    print(f"¡Hola, {nombre}!")
decir_hola("Alice")

#¡Hola, Alice!
#¡Hola, Alice!
#¡Hola, Alice!


""" 
Decordaores utiles
"""


from dataclasses import dataclass

@dataclass
class Persona:
    dedos = 10
    nombre: str
    edad: int
    _dni: int

    def __init__(self, nombre, edad, dni, tarjeta):
        self.nombre = nombre
        self.edad = edad
        self._dni = dni
        self.__tarjeta = tarjeta

    @property
    def dni(self):
        return self._dni

    @classmethod
    def perder_dedo(cls):
        cls.dedos -= 1
        return cls.dedos

    @staticmethod
    def mi_metodo_estatico():
        return "Este es un método estático."


p = Persona("Alice", 30, 123, 456)
print(p)
print(p.dni)
print(p.dni)
print(p.mi_metodo_estatico())

print(p.dedos)
Persona.perder_dedo()
p.perder_dedo()
print(p.dedos)

p2 = Persona("P2", 11, 222, 333)
print(f"P2 tambien tiene {p2.dedos} dedos")
