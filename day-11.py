 #=== Nivel 1 ===

import math
import statistics

def sumar_dos_numeros(a, b):
    return a + b

def area_circulo(radio):
    return math.pi * radio * radio

def sumar_todos(*args):
    if all(isinstance(i, (int, float)) for i in args):
        return sum(args)
    else:
        return "Todos los elementos deben ser números"

def convertir_celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def checar_estacion(mes):
    mes = mes.lower()
    if mes in ['diciembre', 'enero', 'febrero']:
        return 'Invierno'
    elif mes in ['marzo', 'abril', 'mayo']:
        return 'Primavera'
    elif mes in ['junio', 'julio', 'agosto']:
        return 'Verano'
    elif mes in ['septiembre', 'octubre', 'noviembre']:
        return 'Otoño'
    else:
        return 'Mes inválido'

def calcular_pendiente(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

def resolver_ecuacion_cuadratica(a, b, c):
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        return "No hay soluciones reales"
    x1 = (-b + math.sqrt(discriminante)) / (2 * a)
    x2 = (-b - math.sqrt(discriminante)) / (2 * a)
    return (x1, x2)

def imprimir_lista(lista):
    for item in lista:
        print(item)

def revertir_lista(lista):
    reversa = []
    for i in reversed(lista):
        reversa.append(i)
    return reversa

def capitalizar_elementos(lista):
    return [item.capitalize() for item in lista]

def agregar_elemento(lista, elemento):
    lista.append(elemento)
    return lista

def remover_elemento(lista, elemento):
    if elemento in lista:
        lista.remove(elemento)
    return lista

def suma_numeros(n):
    return sum(range(n + 1))

def suma_impares(n):
    return sum(i for i in range(n + 1) if i % 2 != 0)

def suma_pares(n):
    return sum(i for i in range(n + 1) if i % 2 == 0)

# === Nivel 2 ===

def pares_e_impares(numero):
    pares = sum(1 for i in range(numero + 1) if i % 2 == 0)
    impares = numero + 1 - pares
    print(f"Número de pares: {pares}")
    print(f"Número de impares: {impares}")

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def esta_vacio(valor):
    return not bool(valor)

def calcular_media(lista):
    return statistics.mean(lista)

def calcular_mediana(lista):
    return statistics.median(lista)

def calcular_moda(lista):
    return statistics.mode(lista)

def calcular_rango(lista):
    return max(lista) - min(lista)

def calcular_varianza(lista):
    return statistics.variance(lista)

def calcular_std(lista):
    return statistics.stdev(lista)

# === Nivel 3 ===

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def todos_unicos(lista):
    return len(lista) == len(set(lista))

def mismo_tipo(lista):
    return all(isinstance(i, type(lista[0])) for i in lista)

def variable_valida(nombre):
    import keyword
    return nombre.isidentifier() and not keyword.iskeyword(nombre)

def idiomas_mas_hablados(paises, top=10):
    from collections import Counter
    idiomas = []
    for pais in paises:
        idiomas.extend(pais["languages"])
    contador = Counter(idiomas)
    return contador.most_common(top)

def paises_mas_poblados(paises, top=10):
    return sorted(paises, key=lambda x: x['population'], reverse=True)[:top]
