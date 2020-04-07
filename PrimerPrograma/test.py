titulo = "Bienvenido al test que te ayudara a saber si tu perro es un bulldog frances!"
print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")

puntuacion = 0

opcion=input("""¿Tu perro se tira pedos?
A - No, nunca
B - A veces, no muy frecuente
C - Si, muchisimos!
Respuesta: """)
print("\n")

if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("Las opciones son A, B y C")
    exit()


opcion=input("""¿Tu perro tose como un señor al beber agua?
A - ¿Como un señor?
B - No
C - Si, siempre
Respuesta: """)
print("\n")

if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("Las opciones son A, B y C")
    exit()




opcion=input("""¿Tu perro ronca cuando duerme?
A - No
B - A veces, depende de la posicion
C - Si, siempre
Respuesta: """)
print("\n")

if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("Las opciones son A, B y C")
    exit()


if puntuacion <= 10:
    print("No tienes un bullgod frances")
elif puntuacion >= 25:
    print("¿Estas desccribiendo a Tyson o a un hermano gemelo?")
else:
    print("Tienes un Bulldog frances")







