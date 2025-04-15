# Actividad 1

print("-----Actividad 1-----")

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
print(precios_frutas) # Imprime el diccionario original

precios_frutas['Naranja'] = 1200 # Agrega un nuevo elemento al diccionario
precios_frutas['Manzana'] = 1500 # Agrega un nuevo elemento al diccionario
precios_frutas['Pera'] = 2300 # Agrega un nuevo elemento al diccionario

print(precios_frutas) # Imprime el diccionario actualizado

# Actividad 2
print("-----Actividad 2-----")

precios_frutas ['Banana'] = 1330
precios_frutas ['Manzana'] = 1700
precios_frutas ['Melón'] = 2800

print(precios_frutas) # Imprime el diccionario actualizado para el ejercicio 2

# Actividad 3
print("-----Actividad 3-----")

lista_frutas = list(precios_frutas.keys()) # Convierte las claves del diccionario en una lista de frutas
print(lista_frutas) # Imprime la lista de frutas

# Otra forma de hacerlo
for fruta in lista_frutas: # Itera sobre la lista de frutas
    print(fruta) # Imprime cada fruta de la lista

# Actividad 4
print("-----Actividad 4-----")

class Persona:
    def __init__(self, nombre, pais, edad):
        self.nombre = nombre
        self.pais = pais
        self.edad = edad

    def saludar(self):
        print(f"¡Hola!,soy {self.nombre},vivo en {self.pais} y tengo {self.edad} años.")

# Creacion del objeto aunque no se pida en la actividad, para probar la clase
persona1 = Persona("David", "Argentina", 34)
persona1.saludar() # Llama al metodo saludar de la clase Persona

# Actividad 5
print("-----Actividad 5-----")
import math

class Circulo:

    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

# Creacion del objeto aunque no se pida en la actividad, para probar la clase
circulo1 = Circulo(5)
print(f"Area: {circulo1.calcular_area():.2f}")
print(f"Perímetro: {circulo1.calcular_perimetro():.2f}")

# Actividad 6
print("-----Actividad 6-----")

def balanceado(cadena):
    # Diccionario para relacionar parentesis de apertura y cierre
    pares = {')': '(', '}': '{', ']': '['}
    pila = []

    for caracter in cadena:
        if caracter in pares.values():
            # Si es un parentesis de apertura, lo añadimos a la pila
            pila.append(caracter)
        elif caracter in pares.keys():
            # Si es un parentesis de cierre, verificamos la pila
            if not pila or pila.pop() != pares[caracter]:
                return False

    # Si la pila está vacía al final, los parentesis esten balanceados
    return not pila

# Ejemplo de uso
print(balanceado("({[]})"))  # → True
print(balanceado("{{[]}"))   # → False
print(balanceado(")}][{("))  # → False
print(balanceado(")}][{(()"))  # → False
print(balanceado("([)]"))  # → False

# Actividad 7
print("-----Actividad 7-----")

from collections import deque

class Banco:
    def __init__(self):
        self.cola = deque()

    def encolar(self, cliente):
        """Agrega un cliente a la cola (encolar)."""
        self.cola.append(cliente)
        print(f"Cliente '{cliente}' agregado a la cola.")

    def desencolar(self):
        """Atiende al cliente en el frente de la cola (desencolar)."""
        if not self.esta_vacia():
            cliente = self.cola.popleft()
            print(f"Atendiendo al cliente: {cliente}")
            # Mostrar el siguiente cliente automáticamente después de atender
            if not self.esta_vacia():
                print(f"Siguiente cliente: {self.cola[0]}")
            else:
                print("No hay más clientes en la fila.")
            return cliente
        else:
            print("No hay clientes en la fila para atender.")
            return None

    def siguiente_cliente(self):
        """Muestra al siguiente cliente en la fila, sin atenderlo."""
        if not self.esta_vacia():
            print(f"Siguiente cliente: {self.cola[0]}")
            return self.cola[0]
        else:
            print("No hay clientes en la fila.")
            return None

    def esta_vacia(self):
        """Verifica si la cola está vacía."""
        return len(self.cola) == 0


# Ejemplo de uso:
banco = Banco()

# Agregar clientes a la cola
banco.encolar("Cliente 1")
banco.encolar("Cliente 2")
banco.encolar("Cliente 3")

# Mostrar el siguiente cliente
banco.siguiente_cliente()

# Atender clientes con la mejora
banco.desencolar()
banco.desencolar()
banco.desencolar()

# Intentar atender cuando la fila está vacía
banco.desencolar()

# Actividad 8
print("-----Actividad 8-----")

class Nodo:
    def __init__(self, valor):
        self.valor = valor  # Valor almacenado en el nodo
        self.siguiente = None  # Referencia al siguiente nodo

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None  # La lista comienza vacía, sin cabeza

    def insertar_al_inicio(self, valor):
        """Inserta un nuevo nodo al inicio de la lista."""
        nuevo_nodo = Nodo(valor)  # Crear un nodo con el valor dado
        nuevo_nodo.siguiente = self.cabeza  # El nuevo nodo apunta al nodo actual de la cabeza
        self.cabeza = nuevo_nodo  # Actualizamos la cabeza de la lista al nuevo nodo

    def recorrer(self):
        """Recorre la lista y muestra los valores almacenados."""
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            print(nodo_actual.valor, end=" -> ")
            nodo_actual = nodo_actual.siguiente
        print("None")  # Indica el final de la lista


# Ejemplo de uso:
lista = ListaEnlazada()
lista.insertar_al_inicio(10)
lista.insertar_al_inicio(20)
lista.insertar_al_inicio(30)

print("Valores en la lista enlazada:")
lista.recorrer()

# Actividad 9
print("-----Actividad 9-----")

class Nodo:
    def __init__(self, dato):
        self.dato = dato  # El valor del nodo
        self.siguiente = None  # Puntero al siguiente nodo

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None  # La lista comienza vacía

    def insertar(self, dato):
        """Inserta un nuevo nodo al inicio de la lista."""
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def recorrer(self):
        """Recorre la lista y muestra los valores almacenados."""
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

    def invertir(self):
        """Invierte la lista enlazada."""
        previo = None
        actual = self.cabeza
        while actual:
            siguiente = actual.siguiente  # Guardamos el siguiente nodo
            actual.siguiente = previo  # Invertimos el enlace
            previo = actual  # Movemos 'previo' hacia el nodo actual
            actual = siguiente  # Movemos 'actual' hacia el siguiente nodo
        self.cabeza = previo  # Actualizamos la cabeza al ultimo nodo

# Ejemplo de uso:
lista = ListaEnlazada()
lista.insertar(3)
lista.insertar(2)
lista.insertar(1)

print("Lista original:")
lista.recorrer()

lista.invertir()

print("Lista invertida:")
lista.recorrer()
