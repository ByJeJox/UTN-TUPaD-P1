# Actividad 1
print("-----Actividad 1-----")

# Definicion de la funciones
def imprimir_hola_mundo():
    print("Hola Mundo!")

# Programa principal
imprimir_hola_mundo()

# Actividad 2
print("-----Actividad 2-----")

# Definicion de la funciones
def saludar_usuario(nombre):
    print(f"Hola, {nombre}!")

# Programa principal
nombre_usuario = input("Ingrese su nombre: ")
saludar_usuario(nombre_usuario)

# Actividad 3
print("-----Actividad 3-----")

# Definicion de la funciones
def informacion_personall(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Programa principal
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su residencia: ")
informacion_personall(nombre, apellido, edad, residencia)

# Actividad 4
print("-----Actividad 4-----")

# Definicion de la funciones
def validar_numero_positivo():
    numero = float(input("Por favor, ingresa un numero positivo para el radio del circulo: "))
    while numero <= 0:
        print("El numero debe ser positivo. Intenta nuevamente.")
        numero = float(input("Por favor, ingresa un numero positivo para el radio del circulo: "))
    return numero

def calcular_area_circulo(radio):
    area = 3.14 * radio ** 2
    print("El area del circulo es:", area)

def  calcular_perimetro_circulo(radio):
    perimetro = 2 * 3.14 * radio
    print("El perimetro del circulo es:", perimetro)

# Programa principal
radio = validar_numero_positivo()
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)

# Actividad 5
print("-----Actividad 5-----")

# Definicion de la funciones
def validar_segundos():
    segundos = int(input("Por favor, ingresa una cantidad positiva de segundos: "))
    while segundos <= 0:
        print("El numero debe ser positivo. Intenta nuevamente.")
        segundos = int(input("Por favor, ingresa una cantidad positiva de segundos: "))
    return segundos

def segundos_a_horas(segundos):
    horas = segundos // 3600
    print(f"{segundos} segundos equivalen a {horas} horas")

# Programa principal
segundos = validar_segundos()
segundos_a_horas(segundos)

# Actividad 6
print("-----Actividad 6-----")

# Definicion de la funciones
def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Programa principal
numero = int(input("Ingrese un numero para mostrar su tabla de multiplicar: "))
tabla_multiplicar(numero)

# Actividad 7
print("-----Actividad 7-----")

# Definicion de la funciones
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Error: no se puede dividir por cero"
    
    print(f"La suma entre {a} y {b} es: {suma}")
    print(f"La resta entre {a} y {b} es: {resta}")
    print(f"La multiplicacion entre {a} y {b} es: {multiplicacion}")
    print(f"La division entre {a} y {b} es: {division}")

# Programa principal
a = float(input("Ingrese el primer numero para ver una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos: "))
b = float(input("Ingrese el segundo numero para ver una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos: "))
operaciones_basicas(a, b)

# Actividad 8
print("-----Actividad 8-----")

# Definicion de la funciones
def calcular_imc(peso, altura):
    while peso <= 0:
        peso = float(input("El peso debe ser un valor positivo. Por favor, ingresa su peso nuevamente: "))
    while altura <= 0:
        altura = float(input("La altura debe ser un valor positivo. Por favor, ingresa su altura nuevamente: "))
    
    imc = peso / (altura ** 2)
    print(f"Su indice de masa corporal (IMC) es: {imc:.2f}")

# Programa principal
peso = float(input("Por favor, ingresa su peso en kilogramos: "))
altura = float(input("Por favor, ingresa su altura en metros: "))
calcular_imc(peso, altura)

# Actividad 9
print("-----Actividad 9-----")

# Definicion de la funciones
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")

# Programa principal
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
celsius_a_fahrenheit(celsius)

# Actividad 10
print("-----Actividad 10-----")

# Definicion de la funciones
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    print(f"El promedio de los tres numeros es: {promedio:.2f}")

# Programa principal
a = float(input("Ingrese el primer numero para obtener el promedio: "))
b = float(input("Ingrese el segundo numero para obtener el promedio: "))
c = float(input("Ingrese el tercer numero para obtener el promedio: "))
calcular_promedio(a, b, c)