# Actividad 1

for i in range(100+1):
    print(i)

# Actividad 2
print("-----Actividad 2-----")

numero = int(input("Ingrese un numero entero: "))
digitos = len(str(numero))
print(f"El número {numero} tiene {digitos} digitos.")

# Actividad 3
print("-----Actividad 3-----")
suma = 0

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

for i in range(num1, num2+1):
    suma += i
print(f"La suma de los números entre {num1} y {num2} es: {suma}")

# Actividad 4
print("-----Actividad 4-----")

suma = 0

num = int(input("Ingrese un numero para ser sumado, para finalizar ingrese un 0: "))
while num != 0:
    suma += num
    num = int(input("Ingrese un numero: "))
print(f"La suma de los numeros ingresados es: {suma}")

# Actividad 5
print("-----Actividad 5-----")
import random

num_aleatorio = random.randint(1, 9)
intentos = 1

num = int(input("Ingrese un numero entre 1 y 9: "))
while num != num_aleatorio:
    intentos += 1
    num = int(input("Incorrecto, ingrese nuevamente un numero entre 1 y 9: "))
print(f"Numero correcto luego de {intentos} intentos.")


# Actividad 6
print("-----Actividad 6-----")

num1 = 100
num2 = 0

for i in range(num1, num2-1, -2):
    print(i)

# Actividad 7
print("-----Actividad 7-----")

num = int(input("Ingrese un numero entero positivo: "))
while num <= 0:
    print("El numero ingresado no es positivo.")
    num = int(input("Ingrese un numero entero positivo: "))

suma = 0
i = 0

while i <= num:
    suma += i
    i += 1
print(f"La suma de los numeros entre 0 y {num} es: {suma}")


# Actividad 8
print("-----Actividad 8-----")

cant_numeros = 0
num_par = 0
num_impar = 0  
num_positivo = 0
num_negativo = 0

while cant_numeros < 100:
    num = int(input("Ingrese un numero: "))
    if num % 2 == 0:
        num_par += 1
    elif num % 2 != 0:
        num_impar += 1
    if num > 0:
        num_positivo += 1
    elif num < 0:
        num_negativo += 1

    cant_numeros += 1

print(f"Cantidad de numeros pares: {num_par}")
print(f"Cantidad de numeros impares: {num_impar}")
print(f"Cantidad de numeros positivos: {num_positivo}")
print(f"Cantidad de numeros negativos: {num_negativo}")

# Actividad 9
print("-----Actividad 9-----")

cant_numeros = 0
suma = 0

while cant_numeros < 100:
    num = int(input("Ingrese un numero entero: "))
    suma += num 
    cant_numeros += 1

media = suma / cant_numeros
print(f"La media de los numeros ingresados es: {media}")

# Actividad 10
print("-----Actividad 10-----")

num = int(input("Ingrese un numero para ser invertido: "))

num_original = num  
num_invertido = 0  

while num != 0:  
    digito = num % 10  
    num_invertido = num_invertido * 10 + digito 
    num //= 10  
print(f"El número {num_original} invertido es: {num_invertido}")
