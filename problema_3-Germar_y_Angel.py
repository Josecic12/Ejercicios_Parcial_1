import random
import time

def generar_lista(n):
    return [random.randint(1, 1000) for _ in range(n)]

def busqueda_lineal(lista, objetivo):
    for i, num in enumerate(lista):
        if num == objetivo:
            return i  
    return -1

def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio 
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

def medir_tiempo(funcion, *args):
    inicio = time.time()
    resultado = funcion(*args)
    fin = time.time()
    return resultado, fin - inicio

n = 500
lista = generar_lista(n)
lista_ordenada = sorted(lista)

print("Lista de números:")
print(lista)

objetivo = int(input("Ingrese el número que desea buscar: "))

resultado_lineal, tiempo_lineal = medir_tiempo(busqueda_lineal, lista, objetivo)

resultado_binario, tiempo_binario = medir_tiempo(busqueda_binaria, lista_ordenada, objetivo)

print(f"\nResultados para buscar {objetivo}:")
if resultado_lineal != -1:
    print(f"Búsqueda lineal: Encontrado en la posición {resultado_lineal}")
else:
    print("Búsqueda lineal: No encontrado")
print(f"Tiempo de ejecución (búsqueda lineal): {tiempo_lineal:.6f} segundos")

if resultado_binario != -1:
    print(f"Búsqueda binaria: Encontrado en la posición {resultado_binario}")
else:
    print("Búsqueda binaria: No encontrado")
print(f"Tiempo de ejecución (búsqueda binaria): {tiempo_binario:.6f} segundos")

print(f"\nLa búsqueda {'lineal' if tiempo_lineal < tiempo_binario else 'binaria'} fue más rápida en este caso.")
print(f"Diferencia de tiempo: {abs(tiempo_lineal - tiempo_binario):.6f} segundos")