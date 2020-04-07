import random
print("\nEn este juego vas a tener que cruzar una selva para llegar hasta un tesoro\n"
"escondido, no sabes que sorpresas te puede deparar esta aventura asi que tienes\n"
"que estar atento a todos los detalles, cada paso que das, puede ser el ultimo.")
input("\n¿Estas preparado? ")
print("\nVamos alla! \n")
print("""Llegas a la selva en helicoptero, tu equipo te acerca lo maximo posible al punto
donde creeis que puede estar en tesoro... En este punto ya tienes que tomar tu primera
decision! no tienes espacio en tu mochila asi que tienes que escoger entre estos dos
objetos:""")
equipo=input("""\n¿Cuerda para escalar [E] o Tirachinas [T]? """)
if equipo == "E":
    print("\nMetes la cuerda en la mochila y ya estas preparado!")
    equipo = "cuerda"
if equipo == "e":
    print("\nMetes la cuerda en la mochila! ya estas preparado!")
    equipo = "cuerda"
if equipo == "T":
    print("\nMetes el tirachinas en la mochila! ya estas preparado!")
    equipo = "tirachinas"
if equipo == "t":
    equipo = "tirachinas"
    print("\nMetes el tirachinas en la mochila! ya estas preparado!")
print("\nPerfecto! ahora que ya lo tienes todo, a saltaaar!!")
print("""\nCuando estas cayendo tu paracaidas se enreda en un arbol, tienes que cortar la
cuerda para caer. Todo bajo control! no ha sido el mejor aterrizaje pero ya
estas en tierra sano y salvo. Ahora toca situarte en el mapa y empezar a moverte
hacia el tesoro.\n""")
input("¿Te llevas el paracaidas [S] o lo dejas colgado en el arbol [N]? ")  # Esto no servira para nada
if equipo == "tirachinas":
    print("""\nEmpiezas a caminar, te encuentras con un rio y lo sigues por algunos kilometros,
de repente se cruza en tu camino un cocodrilo que esta justo por donde tienes 
que pasar, tienes que decidir que hacer: \n""")
    decision_cocodrilo = input("A - Atacalo desde la distancia con el tirachinas para hacer que se mueva.\n"
    "B - Acercate haciendo mucho ruido con el agua y las piedras para asustarlo y que huya.\n"
    "C - Sientate a esperar hasta que se vaya.\n"
    "Seleccione una opcion: ")
    if decision_cocodrilo == "A":
        print("\nLo conseguiste! ha venido bien tener el tirachinas! sigues tu camino.. \n ")
        print("Sigues caminando y llegas a una zona de dificil acceso, tienes dos opciones para cruzarla:\n")
        input("A - Te balanceas de un lado a otro utilizando las lianas de un arbol\n"
              "B - Cruzar con mucho cuidado utilizando un puente de madera\n"
              "Selecciona una opcion: ")

        print("\nTe caes! no fue una buena idea. A pesar del dolor, puedes continuar. Ahora\n" 
                "tienes que escalar...")
        print("\nMala noticia! no tienes una cuerda para escalar, te tienes que desviar e intentar sobrevivir\n"
              "olvida el tesoro, ahora tu objetivo es sobrevivir...\nFIN")
        exit()
    if decision_cocodrilo == "B":
        print("\nLo conseguiste! era una opcion arriesgada pero ha salido bien\n")
        print("Sigues caminando y llegas a una zona de dificil acceso, tienes dos opciones para cruzarla:\n")
        input("A - Te balanceas de un lado a otro utilizando las lianas de un arbol\n"
                                    "B - Cruzar con mucho cuidado utilizando un puente de madera\n"
                                    "Selecciona una opcion: ")

        print("\nTe caes! no fue una buena idea. A pesar del dolor, puedes continuar. Ahora\n" 
                "tienes que escalar...")
        print("\nMala noticia! no tienes una cuerda para escalar, te tienes que desviar e intentar sobrevivir\n"
              "olvida el tesoro, ahora tu objetivo es sobrevivir...\nFIN")
        exit()
    if decision_cocodrilo == "C":
        print("\nTe quedas dormido y te muerde una serpiente; mueres envenenado..\nFIN")
        exit()
if equipo == "cuerda":
    print("""\nEmpiezas a caminar, te encuentras con un rio y lo sigues por algunos kilometros,
de repente se cruza en tu camino un cocodrilo que esta justo por donde tienes 
que pasar, tienes que decidir que hacer: \n""")
    decision_cocodrilo = input("A - Acercate haciendo mucho ruido con el agua y las piedras para asustarlo y que huya.\n"
    "B - Sientate a esperar hasta que se vaya.\n"
    "Seleccione una opcion: ")
    if decision_cocodrilo == "A":
        print("\nLo conseguiste! era una opcion arriesgada pero ha salido bien\n")
        print("Sigues caminando y llegas a una zona de dificil acceso, tienes dos opciones para cruzarla:\n")
        input("A - Te balanceas de un lado a otro utilizando las lianas de un arbol\n"
              "B - Cruzar con mucho cuidado utilizando un puente de madera\n"
              "Selecciona una opcion: ")

        print("""\nTe caes! no fue una buena idea. A pesar del dolor, puedes continuar. Ahora 
    tienes que escalar...""")
        print("\nHa sido una buena decision traer la cuerda para escalar! Consigues salir del agujero en el que\n"
              "quedaste atrapado... \n")
        adivinanza = random.randint(1, 10)
        print("Despues de caminar durante 4 horas, llegas finalmente a una edificacion antigua con cierto misticismo\n"
              "consigues entrar, sigues adentrandote hasta que llegas a la sala principal y VES EL TESORO!!!!\n"
              "Solo te separa de el un guardian del tesoro, este guardian te dice que tienes un unico intento para\n"
              "adivinar un numero del 1 al 10 y el tesoro sera tuyo.. ")
        intento_adivinanza = int(input("¿Que numero dices?: "))
        if intento_adivinanza == adivinanza:
            print("ENHORABUENA! El tesoro es tuyo!")
            exit()

        if intento_adivinanza <= 0:
                print("El guardian considera tu respuesta una falta de respeto, su peticion fue muy clara, tenia que\n"
                      "ser un numero del  1 al 10.. TE MATA DE MANERA DESPIADADA!\n"
                      "FIN")
                exit()

        if intento_adivinanza > 10:
                print("El guardian considera tu respuesta una falta de respeto, su peticion fue muy clara, tenia que\n"
                      "ser un numero del  1 al 10.. TE MATA DE MANERA DESPIADADA!\n"
                      "FIN")
                exit()
        elif intento_adivinanza != adivinanza:
                print("Has perdido! El guardian te mata... el numero ganador era {}".format(adivinanza))
                exit()
    else:
        print("\nTe quedas dormido y te muerde una serpiente; mueres envenenado..\nFIN")
        exit()
