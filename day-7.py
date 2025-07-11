# -----------------------------------
# 🧩 Ejercicios: Nivel 1
# -----------------------------------

# Conjunto de empresas tecnológicas
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# 1. ¿Cuál es la longitud del conjunto?
print("Longitud del conjunto it_companies:", len(it_companies))

# 2. Agrega 'Twitter' al conjunto
it_companies.add('Twitter')
print("Después de agregar 'Twitter':", it_companies)

# 3. Inserta múltiples empresas a la vez
it_companies.update(['Intel', 'Cisco', 'HP'])
print("Después de agregar varias empresas:", it_companies)

# 4. Elimina una empresa (por ejemplo, 'HP')
it_companies.remove('HP')  # remove lanza error si el elemento no existe
print("Después de eliminar 'HP':", it_companies)

# 5. Diferencia entre remove y discard:
# remove(): lanza un error si el elemento no existe
# discard(): no lanza error si el elemento no existe
it_companies.discard('Netflix')  # No existe, pero no dará error

# -----------------------------------
# 🔁 Ejercicios: Nivel 2
# -----------------------------------

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# 1. Une los conjuntos A y B
union_AB = A.union(B)
print("Unión de A y B:", union_AB)

# 2. Encuentra la intersección de A y B
interseccion_AB = A.intersection(B)
print("Intersección de A y B:", interseccion_AB)

# 3. ¿A es subconjunto de B?
print("¿A es subconjunto de B?", A.issubset(B))

# 4. ¿A y B son conjuntos disjuntos?
print("¿A y B son disjuntos?", A.isdisjoint(B))

# 5. Une A con B y B con A (el resultado será el mismo)
print("A unión B:", A.union(B))
print("B unión A:", B.union(A))

# 6. Diferencia simétrica (elementos que están en un conjunto pero no en ambos)
diferencia_simetrica = A.symmetric_difference(B)
print("Diferencia simétrica entre A y B:", diferencia_simetrica)

# 7. Elimina los conjuntos A y B completamente
del A
del B
# print(A) daría error porque A ya fue eliminado

# -----------------------------------
# 🎓 Ejercicios: Nivel 3
# -----------------------------------

# 1. Convierte la lista de edades a un conjunto y compara la longitud
edades = [22, 19, 24, 25, 26, 24, 25, 24]
conjunto_edades = set(edades)
print("Longitud de la lista original:", len(edades))
print("Longitud del conjunto (sin duplicados):", len(conjunto_edades))

# 2. Diferencias entre tipos de datos:
"""
- String (cadena): texto, por ejemplo: "Hola Mundo"
- Lista (list): colección ordenada y modificable, por ejemplo: [1, 2, 3]
- Tupla (tuple): colección ordenada e inmutable, por ejemplo: (1, 2, 3)
- Conjunto (set): colección desordenada y sin duplicados, por ejemplo: {1, 2, 3}
"""

# 3. ¿Cuántas palabras únicas hay en la siguiente frase?
frase = "Soy profesor y me encanta inspirar y enseñar a las personas"
palabras = frase.split()             # Divide la frase en palabras
palabras_unicas = set(palabras)     # Convierte a conjunto para eliminar duplicados
print("Palabras únicas:", palabras_unicas)
print("Cantidad de palabras únicas:", len(palabras_unicas))
