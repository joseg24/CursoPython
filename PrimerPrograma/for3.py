"""
EJERCICIO FALLIDO

lista_numeros = []
import numbers

while True:
    numeros = int(input("¿Que numeros quieres añadir a la lista?" ))
    lista_numeros.append(numeros)
    print("El numero mas grande de la lista es {} y el numero mas pequeño de la lista es {}".format(max(lista_numeros), min(lista_numeros)))

"""
"""
SOLUCION WHILE

lista_numeros = []

numero_introducido = int(input("Introduzca un numero en la lista... "))
lista_numeros.append(numero_introducido)

while input("¿Desea introducir otro numero? [S/N] ") == "S":
    numero_introducido = int(input("Introduzca un numero en la lista... "))
    lista_numeros.append(numero_introducido)
"""

"""
SOLUCION PRO 1

numeros_introducidos = input("Introduzca los numeros separados por comas: ")
numeros_usuario = numeros_introducidos.split(",")
numeros_usuario_int = []

for numero in numeros_usuario:
    numeros_usuario_int.append(int(numero))
"""




numeros_introducidos = input("Introduzca los numeros separados por comas: ")
numeros_usuario = numeros_introducidos.split(",")
numeros_usuario = [int(numero) for numero in numeros_usuario] #List comprehesion
"""
TRABAJAR LA LISTA DE FORMA MAS PRO
numeros_usuario = [int(numero) for numero in numeros_introducidos.split(",")]
"""

numero_bajo = numeros_usuario[0]
numero_alto = numeros_usuario[0]


for numero in numeros_usuario[1:]:
    if numero_bajo > numero:
        numero_bajo = numero

    if numero_alto < numero:
        numero_alto = numero


print("El numero alto es: {}, y el numero mas pequeño es: {}".format(numero_alto,numero_bajo))





