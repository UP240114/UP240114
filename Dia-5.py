# 1. Declarar una lista vacía
lista_vacia = []

# 2. Declarar una lista con más de 5 elementos
mi_lista = [1, 2, 3, 4, 5, 6, 7]

# 3. Obtener la longitud de la lista
print("Longitud:", len(mi_lista))

# 4. Obtener el primer, medio y último elemento
print("Primero:", mi_lista[0])
print("Medio:", mi_lista[len(mi_lista)//2])
print("Último:", mi_lista[-1])

# 5. Lista con diferentes tipos de datos
datos_personales = ["César", 22, 1.75, "Soltero", "México"]

# 6. Lista de empresas tecnológicas
empresas_ti = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7. Imprimir la lista
print("Empresas TI:", empresas_ti)

# 8. Número de empresas
print("Cantidad de empresas:", len(empresas_ti))

# 9. Primer, medio y último elemento
print("Primera empresa:", empresas_ti[0])
print("Empresa del medio:", empresas_ti[len(empresas_ti)//2])
print("Última empresa:", empresas_ti[-1])

# 10. Modificar una empresa
empresas_ti[1] = "Alphabet"
print("Modificada:", empresas_ti)

# 11. Agregar una empresa
empresas_ti.append("Intel")
print("Agregada una empresa:", empresas_ti)

# 12. Insertar en el medio
indice_medio = len(empresas_ti) // 2
empresas_ti.insert(indice_medio, "Adobe")
print("Insertada en el medio:", empresas_ti)

# 13. Convertir a mayúsculas (excluyendo IBM)
empresas_ti[0] = empresas_ti[0].upper()  # FACEBOOK
print("Con mayúsculas:", empresas_ti)

# 14. Unir con string
empresas_unidas = '#; '.join(empresas_ti)
print("Unidas como string:", empresas_unidas)

# 15. Verificar si una empresa existe
print("¿Está Google en la lista?", "Google" in empresas_ti)

# 16. Ordenar la lista
empresas_ti.sort()
print("Lista ordenada:", empresas_ti)

# 17. Orden inverso
empresas_ti.reverse()
print("Lista invertida:", empresas_ti)

# 18. Cortar las primeras 3 empresas
print("Primeras 3 empresas:", empresas_ti[:3])

# 19. Cortar las últimas 3 empresas
print("Últimas 3 empresas:", empresas_ti[-3:])

# 20. Obtener empresa(s) del medio
medio = len(empresas_ti) // 2
if len(empresas_ti) % 2 == 0:
    print("Empresas del medio:", empresas_ti[medio-1:medio+1])
else:
    print("Empresa del medio:", empresas_ti[medio])

# 21. Eliminar la primera empresa
empresas_ti.pop(0)
print("Primera eliminada:", empresas_ti)

# 22. Eliminar empresa del medio
medio = len(empresas_ti) // 2
empresas_ti.pop(medio)
print("Medio eliminado:", empresas_ti)

# 23. Eliminar la última empresa
empresas_ti.pop()
print("Última eliminada:", empresas_ti)

# 24. Eliminar todas las empresas
empresas_ti.clear()
print("Lista vacía:", empresas_ti)

# 25. Eliminar la lista completamente
del empresas_ti

# 26. Unir listas frontend y backend
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
stack_completo = front_end + back_end
print("Stack completo:", stack_completo)

# 27. Insertar Python y SQL después de Redux
stack_completo.insert(stack_completo.index('Redux') + 1, 'Python')
stack_completo.insert(stack_completo.index('Python') + 1, 'SQL')
print("Stack actualizado:", stack_completo)

# -------- Nivel 2 --------

# Lista de edades de estudiantes
edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Ordenar edades
edades.sort()
print("Edades ordenadas:", edades)

# Edad mínima y máxima
edad_min = min(edades)
edad_max = max(edades)
print("Edad mínima:", edad_min)
print("Edad máxima:", edad_max)

# Agregar otra vez edad mínima y máxima
edades.append(edad_min)
edades.append(edad_max)
print("Lista con duplicados:", edades)

# Mediana de edad
edades.sort()
mitad = len(edades) // 2
if len(edades) % 2 == 0:
    mediana = (edades[mitad - 1] + edades[mitad]) / 2
else:
    mediana = edades[mitad]
print("Mediana:", mediana)

# Promedio de edad
promedio = sum(edades) / len(edades)
print("Promedio:", promedio)

# Rango
rango = edad_max - edad_min
print("Rango:", rango)

# Comparar valores usando valor absoluto
print("abs(min - promedio):", abs(edad_min - promedio))
print("abs(max - promedio):", abs(edad_max - promedio))

# Lista de países
paises = ['China', 'Rusia', 'EEUU', 'Finlandia', 'Suecia', 'Noruega', 'Dinamarca']

# Obtener país(es) del medio
mitad = len(paises) // 2
if len(paises) % 2 == 0:
    print("Países del medio:", paises[mitad-1:mitad+1])
else:
    print("País del medio:", paises[mitad])

# Dividir en dos mitades
if len(paises) % 2 == 0:
    mitad1 = paises[:mitad]
    mitad2 = paises[mitad:]
else:
    mitad1 = paises[:mitad+1]
    mitad2 = paises[mitad+1:]
print("Primera mitad:", mitad1)
print("Segunda mitad:", mitad2)

# Desempaquetar los primeros tres países y el resto como escandinavos
primero, segundo, tercero, *escandinavos = paises
print("Primeros tres:", primero, segundo, tercero)
print("Países escandinavos:", escandinavos)
