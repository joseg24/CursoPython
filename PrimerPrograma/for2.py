numero = int(input("¿Que numero quieres multiplicar? "))

for multiplo in range(1,11):
    if multiplo % 2 == 0:
        print("{} x {} = {}".format(multiplo, numero, multiplo * numero))


