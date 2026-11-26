#Fran Mendez Gonzalez 26/11/2026
#Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a
#introducir). El programa debe informar de cuantos números introducidos son mayores
#que 0, menores que 0 e iguales a 0.

positivos = 0
negativos = 0
ceros = 0

cantidad = int(input("¿Cuántos números vas a introducir? "))

for i in range(cantidad):
    numero = float(input("Introduce un número: "))

    if numero > 0:
        positivos = positivos + 1
    elif numero < 0:
        negativos = negativos + 1
    else:
        ceros = ceros + 1

print("Números positivos:", positivos)
print("Números negativos:", negativos)
print("Números iguales a cero:", ceros)