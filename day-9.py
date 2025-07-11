# -----------------------------------
# Ejercicios: Nivel 1
# -----------------------------------

# 1. Verificar si el usuario tiene edad para conducir
edad = int(input("Ingresa tu edad: "))
if edad >= 18:
    print("Eres lo suficientemente mayor para conducir.")
else:
    años_faltantes = 18 - edad
    print(f"Necesitas esperar {años_faltantes} año{'s' if años_faltantes > 1 else ''} para poder conducir.")

# 2. Comparar edades entre "yo" y el usuario
mi_edad = 25  # Puedes cambiarla por tu edad real
tu_edad = int(input("Ingresa tu edad: "))
diferencia = abs(mi_edad - tu_edad)

if tu_edad > mi_edad:
    print(f"Eres {diferencia} año{'s' if diferencia > 1 else ''} mayor que yo.")
elif tu_edad < mi_edad:
    print(f"Yo soy {diferencia} año{'s' if diferencia > 1 else ''} mayor que tú.")
else:
    print("Tenemos la misma edad.")

# 3. Comparar dos números introducidos por el usuario
a = int(input("Ingresa el número uno: "))
b = int(input("Ingresa el número dos: "))

if a > b:
    print(f"{a} es mayor que {b}")
elif a < b:
    print(f"{a} es menor que {b}")
else:
    print(f"{a} es igual a {b}")

# -----------------------------------
# Ejercicios: Nivel 2
# -----------------------------------

# 1. Calificación según puntaje
puntaje = int(input("Ingresa el puntaje del estudiante (0-100): "))

if 80 <= puntaje <= 100:
    print("Calificación: A")
elif 70 <= puntaje <= 79:
    print("Calificación: B")
elif 60 <= puntaje <= 69:
    print("Calificación: C")
elif 50 <= puntaje <= 59:
    print("Calificación: D")
elif 0 <= puntaje <= 49:
    print("Calificación: F")
else:
    print("Puntaje inválido")

# 2. Determinar estación del año según mes
mes = input("Ingresa un mes: ").capitalize()

if mes in ['Septiembre', 'Octubre', 'Noviembre']:
    print("La estación es Otoño.")
elif mes in ['Diciembre', 'Enero', 'Febrero']:
    print("La estación es Invierno.")
elif mes in ['Marzo', 'Abril', 'Mayo']:
    print("La estación es Primavera.")
elif mes in ['Junio', 'Julio', 'Agosto']:
    print("La estación es Verano.")
else:
    print("Mes inválido")

# 3. Manejo de lista de frutas
frutas = ['banana', 'naranja', 'mango', 'limón']
nueva_fruta = input("Ingresa el nombre de una fruta: ").lower()

if nueva_fruta in frutas:
    print("Esa fruta ya existe en la lista.")
else:
    frutas.append(nueva_fruta)
    print("Lista de frutas actualizada:", frutas)

# -----------------------------------
# Ejercicios: Nivel 3
# -----------------------------------

persona = {
    'nombre': 'Asabeneh',
    'apellido': 'Yetayeh',
    'edad': 250,
    'pais': 'Finlandia',
    'casado': True,
    'habilidades': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'direccion': {
        'calle': 'Space street',
        'codigo_postal': '02210'
    }
}

# 1. Imprimir la habilidad del medio si existe la clave habilidades
if 'habilidades' in persona:
    habilidades = persona['habilidades']
    medio = len(habilidades) // 2
    print("Habilidad del medio:", habilidades[medio])

# 2. Verificar si la persona tiene habilidad en Python
if 'habilidades' in persona:
    if 'Python' in persona['habilidades']:
        print("La persona tiene la habilidad Python.")
    else:
        print("La persona NO tiene la habilidad Python.")

# 3. Determinar el tipo de desarrollador según habilidades
habilidades = persona.get('habilidades', [])

if set(habilidades) == {'JavaScript', 'React'}:
    print("Es un desarrollador frontend.")
elif {'Node', 'Python', 'MongoDB'}.issubset(habilidades):
    print("Es un desarrollador backend.")
elif {'React', 'Node', 'MongoDB'}.issubset(habilidades):
    print("Es un desarrollador fullstack.")
else:
    print("Título desconocido.")

# 4. Información si está casado y vive en Finlandia
if persona.get('casado') and persona.get('pais') == 'Finlandia':
    print(f"{persona['nombre']} {persona['apellido']} vive en Finlandia. Está casado.")
