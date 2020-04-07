from random import randint

print("Vamos a jugar a un juego! Tienes que adivinar un numero del 1 al 10")
numero = random.randint (1, 10)

intento=int(input("Primer intento: "))
if intento == numero:
    print("Enhorabuena! A la primera!")
elif intento != numero:
    print("Fallo!")
    intento=int(input("Prueba otra vez: "))
    if intento == numero:
    print("Enhorabuena!")
    if intento2 != numero:
    print("No pasa nada! Vuelve a probar por ultima vez")
    intento3=int(input("Cual es tu ultimo numero: "))
    if intento3 == numero:
    print("A la tercera va la vencida!")
    if intento3 != numero:
    print("Has perdido, vuelve a probarlo desde el inicio!")
print("El numero ganador era {}".format(numero))
print("Espero que hayas disfrutado el juego!")







