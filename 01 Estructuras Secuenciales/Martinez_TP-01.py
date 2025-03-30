# Ejercicio 1
print("-----Ejercicio 1-----")

print("Hola Mundo!")

# Ejercicio 2
print("-----Ejercicio 2-----")

nombre = input("Por favor, ingresa tu nombre: ")

print(f"Hola {nombre}!")

# Ejercicio 3
print("-----Ejercicio 3-----")

nombre = input("Por favor, ingresa tu nombre: ")
apellido = input("Por favor, ingresa tu apellido: ")
edad = input("Por favor, ingresa tu edad: ")
lugarDeResidencia = input("Por favor, ingresa tu lugar de residencia: ")

print(f"Te llamas {nombre} {apellido}, tenes {edad} años y vivis en {lugarDeResidencia}.")

# Ejercicio 4
print("-----Ejercicio 4-----")

radio = float(input("Ingresa el radio del círculo: "))
area = 3.14 * radio * radio
perimetro = 2 * 3.14 * radio

print(f"El area del circulo es: {area}")
print(f"El perímetro del circulo es: {perimetro}")

# Ejercicio 5
print("-----Ejercicio 5-----")

segundos = int(input("Por favor, ingresa la cantidad de segundos: "))
horas = segundos // 3600
if horas == 1:
    print(f"{segundos} segundos equivalen a {horas} hora.")
else:
    print(f"{segundos} segundos equivalen a {horas} horas.")

# Ejercicio 6
print("-----Ejercicio 6-----")

numero = int(input("Ingresa un número: "))

print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 10):
    print(f"{numero} x {i} = {numero * i}")

# Ejercicio 7
print("-----Ejercicio 7-----")

num1 = int(input("Ingrese el primer numero (distinto de 0): "))
num2 = int(input("Ingrese el segundo numero (distinto de 0): "))

if num1 != 0 and num2 != 0:
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2  

    print(f"La suma de {num1} y {num2} es: {suma}")
    print(f"La resta de {num1} y {num2} es: {resta}")
    print(f"La multiplicación de {num1} y {num2} es: {multiplicacion}")
    print(f"La división de {num1} por {num2} es: {division}")
else:
    print("Ambos números deben ser distintos de 0. Intentalo de nuevo.")

# Ejercicio 8
print("-----Ejercicio 8-----")

peso = float(input("Ingresa tu peso en kilogramos (kg): "))
altura = float(input("Ingresa tu altura en metros (m): "))
imc = peso / (altura * altura)

print(f"Tu Indice de Masa Corporal (IMC) es: {imc}")

# Ejercicio 9
print("-----Ejercicio 9-----")

celsius = float(input("Ingrese la temperatura en grados Celsius: "))


fahrenheit = (9 / 5) * celsius + 32

# Mostramos el resultado
print(f"{celsius}°C equivalen a {fahrenheit}°F.")

# Ejercicio 10
print("-----Ejercicio 10-----")

num1 = float(input("Ingresa el primer numero: "))
num2 = float(input("Ingresa el segundo numero: "))
num3 = float(input("Ingresa el tercer numero: "))

promedio = (num1 + num2 + num3) / 3

print(f"El promedio de los números {num1}, {num2} y {num3} es: {promedio}")