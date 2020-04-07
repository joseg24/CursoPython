titulo = "\nBienvenido a tu programa para la lista de la compra"
print(titulo + "\n" + "-" * len(titulo))

compra = []
eleccion = None

while eleccion != "Q":
        eleccion = input("¿Que deseas comprar? (Q) para salir.. ")
        if eleccion == "Q":
            pass
        elif eleccion in compra:
            print("{} ya esta en la lista..".format(eleccion))
        else:
            if input("¿Seguro que quiere añadir {} en la lista? [S/N]".format(eleccion)) == "S":
                compra.append(eleccion)

print("Tu lista es:")
print(compra)

