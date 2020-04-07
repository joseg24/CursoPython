titulo = "Este test te ayudara a escoger tu movil"
print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")
so=input("¿Que sistema operativo prefieres?\n"
    "A - iOS\n"
    "B - Android\n"
"Que opcion escoges: ")

if so == "A":
    dinero = input("\n¿Tienes dinero?\n"
    "A - Si\n"
    "B - No\n"
    "Seleccione su opcion: ")

    if dinero == "A":
        print("\nDeberias comprar un iPhone Ultra Pro Max")
    else:
        print("\nDeberias comprar un iPhone de segunda mano")

if so == "B":
    dinero = input("\n¿Tienes dinero?\n"
     "A - Si\n"
     "B - No\n"
     "Seleccione su opcion: ")
    if dinero == "A":
        camara = input("\n ¿Te importa la camara?\n"
        "A - Si\n"
        "B - No\n"
        "Seleccione su opcion: ")
        if camara == "A":
            print("\nDeberias comprar un Google Pixel Supercamara ")

        else:
            print("\nDeberias comprar un Android calidad-precio")

    elif dinero == "B":
        print("\nDeberias comprar un Android Chino de 100€")















