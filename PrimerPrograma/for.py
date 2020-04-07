texto = input("¿Que texto quieres analizar? ")
total_espacios = 0
total_puntos = 0
total_comas = 0
for totales in texto:
    if totales == " ":
        total_espacios += 1
    elif totales == ".":
        total_puntos += 1
    elif totales == ",":
        total_comas += 1
print("En el texto hay {} espacios, {} puntos y {} comas..".format(total_espacios, total_puntos, total_comas))









