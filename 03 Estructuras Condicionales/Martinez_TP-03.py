# Actividad 1
print("-----Actividad 1-----")

edad = int(input("Ingrese su edad: "))

if edad > 18:
    print("Es mayor de edad")

# Actividad 2
print("-----Actividad 2-----")

nota = float(input("Ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")   

# Actividad 3
print("-----Actividad 3-----")

num = int(input("Ingrese un numero: "))

if num % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# Actividad 4
print("-----Actividad 4-----")

edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Es un Niño/a")
elif edad >= 12 and edad < 18:
    print("Es un Adolescente")
elif edad >= 18 and edad < 30:
    print("Es un Adulto/a joven")
else:
    print("Es un Adulto/a")

# Actividad 5
print("-----Actividad 5-----")

contraseña = input("Ingrese la contraseña: ")  

if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# Actividad 6
print("-----Actividad 6-----")

# Las import van arriba pero lo pongo aca para no pisar los ejercicios
import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

if media > mediana > moda:
    sesgo = "Sesgo positivo (a la derecha)"
elif media < mediana < moda:
    sesgo = "Sesgo negativo (a la izquierda)"
else:
    sesgo = "Sin sesgo"

#Resultados
print(f"Lista generada: {numeros_aleatorios}")
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
print(f"Distribucion: {sesgo}")

# Actividad 7
print("-----Actividad 7-----")

palabras = input("Ingrese una frase o palabra")

if palabras[-1] in "aeiouAEIOU":
    palabras += "!"

print(palabras)

# Actividad 8
print("-----Actividad 8-----")

nombre = input("Ingrese su nombre: ")
formato = input("Ingrese: "
"                        1. Si quiere su nombre en mayúsculas"
"                        2. Si quiere su nombre en minúsculas"
"                        3. Si quiere su nombre con la primera letra mayúscula")

if formato == "1":
    print(nombre.upper())
elif formato == "2":
    print(nombre.lower())
elif formato == "3":
    print(nombre.title())
else:
    print("Por favor, ingrese una opción valida")

# Actividad 9
print("-----Actividad 9-----")

magnitud = float(input("Ingrese la magnitud de un terremoto: "))

if magnitud < 3:
    print("Muy leve")
elif magnitud >= 3 and magnitud < 4:
    print("Leve")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte")
else:
    print("Extremo")

# Actividad 10
print("-----Actividad 10-----")

hemisferio = input("Ingrese el hemisferio (N/S): ").upper()
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el dia (1-31): "))

if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    else:
        estacion = "Otoño"
    print(f"Estación en el hemisferio norte: {estacion}")

elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    else:
        estacion = "Primavera"
    print(f"Estación en el hemisferio sur: {estacion}")

else:
    print("Entrada inválida, por favor ingrese 'N' o 'S'.")


