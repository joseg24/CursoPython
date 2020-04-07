euros_a_libras = 1
libras_a_euros = 2
euros_a_dolares = 3
dolares_a_euros = 4

tipo_1 = 0.84
tipo_2 = 1.19
tipo_3 = 1.08
tipo_4 = 0.92

titulo="Bienvenido a nuestro cambiador de divisas" "\n"
print("\n" + titulo + "-" * len(titulo) + "\n")

print("""¿Que operacion desea realizar hoy? 
1 - Cambiar de Euros a Libras
2 - Cambiar de Libras a Euros
3 - Cambiar de Euros a Dolares
4 - Cambiar de Dolares a Euros""")
tipo_de_operacion=input("Seleccione su opcion: ")

importe=float(input("¿Cuantos {} quieres convertir? "))


if tipo_de_operacion == "1":
    cantidad de dinero=float(input(importe.format("Euros")))
    print("Recibiras {} libras".format(importe * tipo_1))
elif tipo_de_operacion == "2":
    print("Recibiras {} €".format(importe * tipo_2))
elif tipo_de_operacion == "3":
    print("Recibiras {} $".format(importe * tipo_3))
elif tipo_de_operacion == "4":
    print("Recibiras {} €".format(importe * tipo_4))
