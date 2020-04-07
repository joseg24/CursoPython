nombre=input("Hola! ¿Cual es tu nombre? ")
a=(int(input("Encantado de conocerte " + nombre + ", necesito que me digas un numero: ")))
print("Perfecto!")
b=(int(input("Ahora dime otro: ")))
c=(int(input("Dime un ultimo numero: ")))
print("El numero mayor entre {}, {} y {} es {}, y el mas pequeño es {}".format(a, b, c, max(a,b,c), min(a,b,c)))
validacion=input("Es correcto? (S/N) ")
if validacion == "S":
    print("Lo se ;)")
if validacion != "S":
    print("No me engañes!")
