# Actividad 1
print("-----Actividad 1-----")

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Solicitar al usuario un numero
num = int(input("Ingrese un numero entero positivo: "))

# Validar que el numero sea positivo
if num < 1:
    print("Ingrese un numero mayor o igual a 1.")
else:
    # Calcular y mostrar los factoriales
    for i in range(1, num + 1):
        print(f"Factorial de {i}: {factorial(i)}")

# Actividad 2
print("-----Actividad 2-----")

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
# Solicitar al usuario un número
num = int(input("Ingresa la posición hasta la que deseas calcular la serie Fibonacci: "))

# Validar que el número sea positivo
if num < 1:
    print("Por favor, ingresa un número mayor o igual a 1.")
else:
    # Mostrar la serie completa hasta la posición indicada
    print("Serie Fibonacci:")
    for i in range(1, num + 1):
        print(fibonacci(i))

# Actividad 3
print("-----Actividad 3-----")

def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

# Solicitar al usuario la base y el exponente
base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

# Validar que el exponente sea positivo
if exponente < 0:
    print("El exponente debe ser un número entero positivo.")
else:
    # Calcular y mostrar la potencia
    resultado = potencia(base, exponente)
    print(f"{base} elevado a {exponente} es: {resultado}")

# Actividad 4
print("-----Actividad 4-----")

def conversor_decimal_a_binario(n):
    if n == 0:
        return ""
    elif n == 1:
        return "1"
    else:
        return conversor_decimal_a_binario(n // 2) + str(n % 2)

# Solicitar al usuario un número decimal positivo
num = int(input("Ingrese un número decimal positivo: "))
# Validar que el número sea positivo   
if num < 0:
    print("Por favor, ingrese un número positivo.")
else:
    # Convertir y mostrar el número en binario
    binario = conversor_decimal_a_binario(num)
    print(f"El número {num} en binario es: {binario}")

# Actividad 5
print("-----Actividad 5-----")

def es_palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

# Solicitar al usuario una palabra o frase
palabra = input("Ingresa una palabra sin espacios ni tildes: ")

if es_palindromo(palabra):
    print(f"La palabra '{palabra}' es un palíndromo.")
else:
    print(f"La palabra '{palabra}' no es un palíndromo.")

# Actividad 6
print("-----Actividad 6-----")

def suma_digitos(n):
    if n == 0:
        return 0
    return n % 10 + suma_digitos(n // 10)

# Pruebas
print(suma_digitos(1234))
print(suma_digitos(9))
print(suma_digitos(305))

# Actividad 7
print("-----Actividad 7-----")

def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

#Pruebas
print(contar_bloques(1))  
print(contar_bloques(2)) 
print(contar_bloques(4))  

# Actividad 8
print("-----Actividad 8-----")

def contar_digitos(n, digito):
    if n == 0:
        return 0
    if n % 10 == digito:
        return 1 + contar_digitos(n // 10, digito)
    else:
        return contar_digitos(n // 10, digito)

#Pruebas

print(contar_digitos(12233421, 2))
print(contar_digitos(5555, 5))
print(contar_digitos(123456, 7))