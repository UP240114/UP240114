# Filtrar solo negativos y ceros
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negativos_y_ceros = [n for n in numbers if n <= 0]

# Aplanar lista de listas de listas
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
lista_aplanada = [num for sublist in list_of_lists for inner in sublist for num in inner]

# Lista de tuplas
lista_tuplas = [(x, 1, x, x**2, x**3, x**4, x**5) for x in range(11)]

# Aplanar lista de países con información extendida
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
info_extendida = [[pais.upper(), pais[:3].upper(), ciudad.upper()] for lista in countries for (pais, ciudad) in lista]

# Convertir a lista de diccionarios
lista_diccionarios = [{'country': pais.upper(), 'city': ciudad.upper()} for lista in countries for (pais, ciudad) in lista]

# Concatenar nombres en una lista
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
nombres_completos = [f"{nombre} {apellido}" for pareja in names for (nombre, apellido) in pareja]

# Lambda para pendiente (slope) y ordenada al origen (y-intercept)
# Pendiente: m = (y2 - y1) / (x2 - x1)
pendiente = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)

# Ordenada al origen: y = mx + b => b = y - mx
ordenada_origen = lambda x, y, m: y - m * x