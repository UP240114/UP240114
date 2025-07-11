# -----------------------------------
# Ejercicios: Nivel 1
# -----------------------------------

# 1. Iterar de 0 a 10 usando for
print("Iterar 0 a 10 usando for:")
for i in range(11):
    print(i, end=' ')
print("\n")

# Iterar de 0 a 10 usando while
print("Iterar 0 a 10 usando while:")
i = 0
while i <= 10:
    print(i, end=' ')
    i += 1
print("\n")

# 2. Iterar de 10 a 0 usando for
print("Iterar 10 a 0 usando for:")
for i in range(10, -1, -1):
    print(i, end=' ')
print("\n")

# Iterar de 10 a 0 usando while
print("Iterar 10 a 0 usando while:")
i = 10
while i >= 0:
    print(i, end=' ')
    i -= 1
print("\n")

# 3. Triángulo de hashes con 7 líneas
print("Triángulo de hashes:")
for i in range(1, 8):
    print('#' * i)
print("\n")

# 4. Cuadrícula 8x8 con #
print("Cuadrícula 8x8:")
for i in range(8):
    for j in range(8):
        print('#', end=' ')
    print()
print("\n")

# 5. Patrón de cuadrados (0 x 0, 1 x 1, ...)
print("Cuadrados de números del 0 al 10:")
for i in range(11):
    print(f"{i} x {i} = {i*i}")
print("\n")

# 6. Iterar lista e imprimir
print("Elementos de la lista:")
lista = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for item in lista:
    print(item)
print("\n")

# 7. Imprimir solo números pares de 0 a 100
print("Números pares de 0 a 100:")
for i in range(0, 101, 2):
    print(i, end=' ')
print("\n")

# 8. Imprimir solo números impares de 0 a 100
print("Números impares de 0 a 100:")
for i in range(1, 101, 2):
    print(i, end=' ')
print("\n")

# -----------------------------------
# Ejercicios: Nivel 2
# -----------------------------------

# 1. Suma de todos los números de 0 a 100
suma_total = 0
for i in range(101):
    suma_total += i
print(f"La suma de todos los números de 0 a 100 es {suma_total}\n")

# 2. Suma de pares e impares
suma_pares = 0
suma_impares = 0
for i in range(101):
    if i % 2 == 0:
        suma_pares += i
    else:
        suma_impares += i
print(f"La suma de los pares es {suma_pares}. La suma de los impares es {suma_impares}\n")

# -----------------------------------
# Ejercicios: Nivel 3
# -----------------------------------

# 1. Extraer países que contienen "land"
# Suponemos que tenemos una lista llamada countries (puedes cambiarla según el archivo que tengas)
countries = [
    "Finland", "Sweden", "Iceland", "Denmark", "Ireland", "Poland", "Thailand", "Netherlands", "England", "Scotland"
]

print("Países que contienen 'land':")
for country in countries:
    if 'land' in country.lower():
        print(country)
print("\n")

# 2. Invertir lista de frutas usando un loop
frutas = ['banana', 'orange', 'mango', 'lemon']
frutas_invertidas = []
for i in range(len(frutas)-1, -1, -1):
    frutas_invertidas.append(frutas[i])

print("Lista invertida de frutas:")
print(frutas_invertidas)
print("\n")

# 3. Total de idiomas en data countries_data.py
# Suponiendo que tenemos una lista de diccionarios llamada countries_data (ejemplo)
countries_data = [
    {'name': 'Finland', 'languages': ['Finnish', 'Swedish'], 'population': 5536146},
    {'name': 'Sweden', 'languages': ['Swedish'], 'population': 10353442},
    {'name': 'Norway', 'languages': ['Norwegian'], 'population': 5421241},
    {'name': 'Denmark', 'languages': ['Danish'], 'population': 5822763},
    {'name': 'Iceland', 'languages': ['Icelandic'], 'population': 366425}
]

idiomas = set()
for country in countries_data:
    for lang in country['languages']:
        idiomas.add(lang)

print(f"Total de idiomas únicos: {len(idiomas)}")
print("\n")

# 4. Diez idiomas más hablados (ejemplo simplificado)
from collections import Counter

# Suponemos que contamos la frecuencia de idiomas en countries_data
contador_idiomas = Counter()
for country in countries_data:
    for lang in country['languages']:
        contador_idiomas[lang] += 1

mas_hablados = contador_idiomas.most_common(10)
print("Los 10 idiomas más hablados:")
for idioma, cuenta in mas_hablados:
    print(f"{idioma}: {cuenta} países")
print("\n")

# 5. Diez países más poblados
paises_ordenados = sorted(countries_data, key=lambda x: x['population'], reverse=True)
print("Los 10 países más poblados:")
for pais in paises_ordenados[:10]:
    print(f"{pais['name']}: {pais['population']}")
