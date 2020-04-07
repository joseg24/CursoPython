from random import randint
import os
VIDA_INICIAL_PIKACHU = 80
VIDA_INICIAL_BULBASAUR = 90
TAMANO_BARRA = 20
vida_actual_pikachu = VIDA_INICIAL_PIKACHU
vida_actual_bulbasaur = VIDA_INICIAL_BULBASAUR
barra_pikachu = int(vida_actual_pikachu * TAMANO_BARRA / VIDA_INICIAL_PIKACHU)
barra_bulbasaur = int(vida_actual_bulbasaur * TAMANO_BARRA / VIDA_INICIAL_BULBASAUR)


print("\nEmpieza el combate entre Pikachu y Bulbasur! ¿estas listo?")
print("Pikachu:    [{}{}] {}/{}".format(barra_pikachu * "#", " " * (TAMANO_BARRA - barra_pikachu), vida_actual_pikachu,
                                            VIDA_INICIAL_PIKACHU))
print("Bulbasaur:  [{}{}] {}/{}\n".format(barra_bulbasaur * "#", " " * (TAMANO_BARRA - barra_bulbasaur),
                                            vida_actual_bulbasaur, VIDA_INICIAL_BULBASAUR))
input("Presiona enter para empezar...")
os.system("cls")

while vida_actual_bulbasaur > 0 and vida_actual_pikachu > 0:
    # Ataque bulbasur
    print("\nAtaca Bulbasur..")
    ataque_bulbasur = randint(1,2)
    if ataque_bulbasur == 1:
        print("utilizando Látigo Cepa!")
        vida_actual_pikachu -= 9
    else:
        print("utilizando Hoja Afilada!")
        vida_actual_pikachu -= 11

    if vida_actual_pikachu <= 0:
        vida_actual_pikachu = 0
        barra_pikachu = int(vida_actual_pikachu * TAMANO_BARRA / VIDA_INICIAL_PIKACHU)
        print("Pikachu:    [{}{}] {}/{}".format(barra_pikachu * "#", " " * (TAMANO_BARRA - barra_pikachu),
                                                vida_actual_pikachu,
                                                VIDA_INICIAL_PIKACHU))
        barra_bulbasaur = int(vida_actual_bulbasaur * TAMANO_BARRA / VIDA_INICIAL_BULBASAUR)
        print("Bulbasaur:  [{}{}] {}/{}\n".format(barra_bulbasaur * "#", " " * (TAMANO_BARRA - barra_bulbasaur),
                                                  vida_actual_bulbasaur, VIDA_INICIAL_BULBASAUR))

        print("\nBulbasur GANA!!")
        exit()

    barra_pikachu = int(vida_actual_pikachu * TAMANO_BARRA / VIDA_INICIAL_PIKACHU)
    print("Pikachu:    [{}{}] {}/{}".format(barra_pikachu * "#", " " * (TAMANO_BARRA - barra_pikachu), vida_actual_pikachu,
                                            VIDA_INICIAL_PIKACHU))
    barra_bulbasaur = int(vida_actual_bulbasaur * TAMANO_BARRA / VIDA_INICIAL_BULBASAUR)
    print("Bulbasaur:  [{}{}] {}/{}\n".format(barra_bulbasaur * "#", " " * (TAMANO_BARRA - barra_bulbasaur),
                                            vida_actual_bulbasaur, VIDA_INICIAL_BULBASAUR))

    #Ataque pikachu
    input("Presiona enter para continuar..")
    os.system("cls")
    print("\nAhora toca el turno a Pikachu!")
    ataque_pikachu = None
    while ataque_pikachu not in ["I", "V", "R", "N"]:
            ataque_pikachu = input("¿Que ataque deseas realizar? [I]mpactrueno, Bola [V]oltio, [R]ayo o [N]o hacer nada: ")
    print("Ataca Pikachu..")
    if ataque_pikachu == "I":
        vida_actual_bulbasaur -= 10
        print("utilizando Impactrueno!")
    elif ataque_pikachu == "V":
        vida_actual_bulbasaur -= 12
        print("utilizando Bola Voltio!")
    elif ataque_pikachu == "R":
        vida_actual_bulbasaur -= 9
        print("utilizando Rayo!")
    elif ataque_pikachu == "N":
        print("Pikachu no ataca en este turno..")

    if vida_actual_bulbasaur <= 0:
        vida_actual_bulbasaur = 0
        barra_pikachu = int(vida_actual_pikachu * TAMANO_BARRA / VIDA_INICIAL_PIKACHU)
        print("Pikachu:    [{}{}] {}/{}".format(barra_pikachu * "#", " " * (TAMANO_BARRA - barra_pikachu),
                                                vida_actual_pikachu,
                                                VIDA_INICIAL_PIKACHU))
        barra_bulbasaur = int(vida_actual_bulbasaur * TAMANO_BARRA / VIDA_INICIAL_BULBASAUR)
        print("Bulbasaur:  [{}{}] {}/{}\n".format(barra_bulbasaur * "#", " " * (TAMANO_BARRA - barra_bulbasaur),
                                                  vida_actual_bulbasaur, VIDA_INICIAL_BULBASAUR))

        print("\nPikachu GANA!!")
        exit()
    barra_pikachu = int(vida_actual_pikachu * TAMANO_BARRA / VIDA_INICIAL_PIKACHU)
    print("Pikachu:    [{}{}] {}/{}".format(barra_pikachu * "#", " " * (TAMANO_BARRA - barra_pikachu), vida_actual_pikachu,
                                                VIDA_INICIAL_PIKACHU))
    barra_bulbasaur = int(vida_actual_bulbasaur * TAMANO_BARRA / VIDA_INICIAL_BULBASAUR)
    print("Bulbasaur:  [{}{}] {}/{}\n".format(barra_bulbasaur * "#", " " * (TAMANO_BARRA - barra_bulbasaur),
                                                  vida_actual_bulbasaur, VIDA_INICIAL_BULBASAUR))
    input("Presiona enter para continuar..")
    os.system("cls")

if vida_actual_bulbasaur > vida_actual_pikachu:
    print("\nBulbasur GANA!!")
else:
    print("\nPikachu GANA!!")































