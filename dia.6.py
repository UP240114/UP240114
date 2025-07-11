# Ejercicios con tuplas en español

# 1. Crear una tupla vacía
tupla_vacia = ()

# 2. Tupla con nombres de hermanas y hermanos
hermanas = ("Ana", "Laura", "Sofía")
hermanos = ("Carlos", "Luis", "Mateo")

# 3. Unir hermanos y hermanas
hermanos_y_hermanas = hermanas + hermanos
print("Hermanos y hermanas:", hermanos_y_hermanas)

# 4. ¿Cuántos hermanos tengo?
print("Número de hermanos:", len(hermanos_y_hermanas))

# 5. Agregar padres a la tupla
miembros_familia = hermanos_y_hermanas + ("Papá", "Mamá")
print("Miembros de la familia:", miembros_familia)

# -------- Nivel 2 --------

# 6. Desempaquetar hermanos y padres
*hermanos_y_hermanas, padre, madre = miembros_familia
print("Hermanos y hermanas desempaquetados:", hermanos_y_hermanas)
print("Padre:", padre)
print("Madre:", madre)

# 7. Crear tuplas de frutas, vegetales y productos animales
frutas = ("Manzana", "Banana", "Uva")
vegetales = ("Zanahoria", "Lechuga", "Espinaca")
productos_animales = ("Leche", "Huevos", "Carne")

# 8. Unir las tuplas en una llamada food_stuff_tp
food_stuff_tp = frutas + vegetales + productos_animales
print("Tupla de alimentos:", food_stuff_tp)

# 9. Convertir la tupla a lista
food_stuff_lt = list(food_stuff_tp)
print("Lista de alimentos:", food_stuff_lt)

# 10. Cortar el/los elemento(s) del medio
medio = len(food_stuff_lt) // 2
if len(food_stuff_lt) % 2 == 0:
    print("Elementos del medio:", food_stuff_lt[medio-1:medio+1])
else:
    print("Elemento del medio:", food_stuff_lt[medio])

# 11. Cortar los primeros y últimos tres elementos
print("Primeros tres elementos:", food_stuff_lt[:3])
print("Últimos tres elementos:", food_stuff_lt[-3:])

# 12. Eliminar completamente la tupla de alimentos
del food_stuff_tp
# print(food_stuff_tp)  # Esto causaría error si se descomenta

# 13. Verificar si un ítem existe en la tupla
nordic_countries = ('Dinamarca', 'Finlandia', 'Islandia', 'Noruega', 'Suecia')

# Verificar si 'Estonia' es un país nórdico
print("¿Estonia es nórdico?", 'Estonia' in nordic_countries)

# Verificar si 'Islandia' es un país nórdico
print("¿Islandia es nórdico?", 'Islandia' in nordic_countries)
