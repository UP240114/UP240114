# -----------------------------------
# Diccionario del perro
# -----------------------------------

# Crear un diccionario vacío llamado 'perro'
perro = {}

# Agregar nombre, color, raza, patas y edad al diccionario del perro
perro['nombre'] = 'Max'
perro['color'] = 'Marrón'
perro['raza'] = 'Labrador'
perro['patas'] = 4
perro['edad'] = 5

print("Diccionario del perro:", perro)

# -----------------------------------
# Diccionario del estudiante
# -----------------------------------

# Crear el diccionario del estudiante con varias claves
estudiante = {
    'nombre': 'Juan',
    'apellido': 'Pérez',
    'genero': 'Masculino',
    'edad': 21,
    'estado_civil': 'Soltero',
    'habilidades': ['Python', 'HTML'],
    'pais': 'México',
    'ciudad': 'Guadalajara',
    'direccion': 'Av. Universidad 123'
}

# Obtener la longitud del diccionario del estudiante
print("Longitud del diccionario del estudiante:", len(estudiante))

# Obtener el valor de 'habilidades' y verificar que es una lista
print("Habilidades:", estudiante['habilidades'])
print("Tipo de datos de habilidades:", type(estudiante['habilidades']))

# Modificar habilidades agregando una o dos habilidades más
estudiante['habilidades'].append('CSS')
estudiante['habilidades'].append('JavaScript')
print("Habilidades actualizadas:", estudiante['habilidades'])

# Obtener las claves del diccionario como lista
print("Claves del diccionario:", list(estudiante.keys()))

# Obtener los valores del diccionario como lista
print("Valores del diccionario:", list(estudiante.values()))

# Convertir el diccionario a una lista de tuplas
print("Diccionario como lista de tuplas:", list(estudiante.items()))

# Eliminar uno de los elementos del diccionario (por ejemplo 'estado_civil')
del estudiante['estado_civil']
print("Diccionario después de eliminar 'estado_civil':", estudiante)

# Eliminar completamente el diccionario del perro
del perro
# print(perro)  # Esto lanzaría un error porque el diccionario ya no existe
