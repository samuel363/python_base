class Persona:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self._dni = dni            # Privado
        # self.__tarjeta = tarjeta # Privado Estricto

    def mostrar_edad(self):
        print(self.edad)

    def modificar_edad(self, edad):
        if 0 > edad < 150:
            return False
        self.edad = edad

    def mostrar_dni(self):
        print(f"dni: {self._dni}")

p = Persona('Samuel', 20, 123)
print(p.nombre)
# Samuel
p.nombre = 'Pablo'
print(p.nombre)
# Pablo
# print(p.__dni)
# Error: 'Persona' object has no attribute '__dni'
p.mostrar_dni()
#dni: 123
p.mostrar_edad()
# 20
p.modificar_edad(21)
p.mostrar_edad()
# 21

""" HERENCIA """


class Trabajador(Persona):
    cargo: str

    def __init__(self, nombre, edad, dni, cargo):
        super().__init__(nombre, edad, dni)
        self.cargo = cargo

    def trabajar(self):
        return "Trabajando!..."

p2 = Trabajador("Roberto", "20", 123, "desarrollador")
print(p2.__dict__)
# {'nombre': 'Roberto', 'edad': '20', '_Persona__dni': 123, 'cargo': 'desarrollador'}
print(p2.trabajar())
# Trabajando!...
