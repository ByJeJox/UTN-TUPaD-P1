# Actividad 1
print("-----Actividad 1-----")

lista_multiplos_4 = list(range(4, 101, 4))
print(lista_multiplos_4)

# Actividad 2
print("-----Actividad 2-----")


mi_lista = ["Python", "Musica", "Dias", "Juegos", "Viajar"]

penultimo = mi_lista[-2]
print(penultimo)

# Actividad 3
print("-----Actividad 3-----")

lista_vacia = []

lista_vacia.append("Python")
lista_vacia.append("Aprender")
lista_vacia.append("Divertido")

print(lista_vacia)

# Actividad 4
print("-----Actividad 4-----")

animales = ["perro", "gato", "conejo", "pez"]

animales[1] = "loro"
animales[-1] = "oso"

print(animales)

# Actividad 5
print("-----Actividad 5-----")

print("Define una lista llamada numeros con los valores [8, 15, 3, 22, 7].\n"
      "Usa la funcion max() para encontrar el valor maximo de la lista y luego lo elimina con el metodo remove().\n"
      "Por ultimo imprime la lista modificada.")

# Actividad 6
print("-----Actividad 6-----")

numeros = list(range(10, 31, 5))
print(numeros[:2])

# Actividad 7
print("-----Actividad 7-----")

autos = ["sedan", "polo", "suran", "gol"]

autos[1] = "camioneta"
autos[2] = "SUV"

print(autos)

# Actividad 8
print("-----Actividad 8-----")

dobles = []

dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

print(dobles)

# Actividad 9
print("-----Actividad 9-----")

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")

print(compras)

# Actividad 10
print("-----Actividad 10-----")


lista_anidada = [
    15,  # Posición lista_anidada[0]
    True,  # Posición lista_anidada[1]
    [25.5, 57.9, 30.6],  # Posición lista_anidada[2]
    False  # Posición lista_anidada[3]
]

print(lista_anidada)



