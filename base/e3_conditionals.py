""" IF """
verdadero = True
if verdadero:  # No es necesario poner "verdadero == True"
    print("Verdadero")
elif verdadero == "Python":     # ELIF
    print("Python")
else:                           # ELSE
    print("Falso")


''' MATCH-CASE (SWITCH)'''
variable = 1
match variable:
    case 1:
        print("1")
    case 2:
        print("2")
    case 3:
        print("3")
    case _:
        print("otro")


""" BUCLES """

""" FOR """
lista = ["a", "b", "c"]
for i in lista:  # Iteramos sobre una lista, que es iterable
    print(i)


""" WHILE """
numero = 0
while numero < 10:
    print(numero, end=" ")
    numero += 1