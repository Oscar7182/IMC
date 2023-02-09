#Se le solicita el nombre
n = input("Su nombre por favor: ")

    #Se pide la edad que siempre es un entero por eso el int()
    #Tambien para validar se usa un bucle el cual se rompe hasta que ingrese un valor valido, lo mismo para las demas validaciones como: la altura, los kilogramos, etc
while True:
    try:
        e = int(input("Su edad en años por favor: "))
    except ValueError:
        print("Ingresa un número")
        continue
    if e <= 0:
        print("Ingresa un número positivo y que tampoco sea 0")
        continue
    else:
        break


    #Como la altura es en metros y no centimetros hay que ponerle punto y por ende es un flotante float()
while True:
    try:
        a = float(input ("Su altura en metros por favor: "))
    except ValueError:
        print("Ingresa un número")
        continue
    if a <= 0:
        print("Ingresa un número positivo y que tampoco sea 0")
        continue
    else:
        break
#Se le dice que la estatura es igual a la altura
est = a
    #La masa en kilogramos si puede tener decimales asi que la dejamos flotante
while True:
    try:
        m = float(input ("Su masa en kilogramos por favor: "))
    except ValueError:
        print("Ingresa un número")
        continue
    if m <= 0:
        print("Ingresa un número positivo y que tampoco sea 0")
        continue
    else:
        break
    #Calculo del IMC, masa (En kilogramos) entre la estatura (En metros) elevada al cuadrado
IMC = m / est**2       
    #Se imprime el nombre
print("Datos de: " + n)

    #Se comprueba si es menor o mayor de edad, si es menor a 18 es menor, si no es mayor edad
if(e < 18):
        print("Es menor de edad")
else:
        print("Es mayor de edad")
    #Imprimimos su IMC
print("IMC: " + str(IMC))

    #Se hacen las distintas validaciones
if IMC >= 0 and IMC <= 15.99 :
        print ("Tiene delgadez severa")
elif IMC >= 16.00 and IMC <= 16.99 :
        print ("Tiene delgadez moderada")
elif IMC >= 17.00 and IMC <= 18.49:
        print ("Tiene delgadez leve")
elif IMC >= 18.50 and IMC <= 24.99 :
        print ("Tiene peso normal")
elif IMC >= 25.00 and IMC <= 29.99:
        print ("Tiene sobrepeso")
elif IMC >= 30.00 and IMC <= 34.99:
        print ("Tiene obesidad leve")
elif IMC >= 35.00 and IMC <= 39.00:
        print ("Tiene obesidad media")
elif IMC >= 40.00:
        print ("Tiene obesidad morbida")