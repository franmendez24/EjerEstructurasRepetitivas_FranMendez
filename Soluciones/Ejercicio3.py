#Fran Mendez Gonzalez 26/11/2026
#Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y
#la media de todos los números introducidos.

suma = 0
contador = 0

numero = float(input("Introduce un número (0 para terminar): "))

while numero != 0:
    suma = suma + numero
    contador = contador + 1

    numero = float(input("Introduce otro número (0 para terminar): "))

if contador > 0:
    media = suma / contador
    print("La suma es:", suma)
    print("La media es:", media)
else:
    print("No se han introducido números")