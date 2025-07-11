import random
import string

# Nivel 1

def random_user_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def user_id_gen_by_user():
    num_chars = int(input("Número de caracteres por ID: "))
    num_ids = int(input("Número de IDs a generar: "))
    for _ in range(num_ids):
        print(''.join(random.choices(string.ascii_letters + string.digits, k=num_chars)))

def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"

# Nivel 2

def list_of_hexa_colors(n):
    return ['#' + ''.join(random.choices('0123456789abcdef', k=6)) for _ in range(n)]

def list_of_rgb_colors(n):
    return [rgb_color_gen() for _ in range(n)]

def generate_colors(tipo, cantidad):
    if tipo == 'hexa':
        return list_of_hexa_colors(cantidad)
    elif tipo == 'rgb':
        return list_of_rgb_colors(cantidad)
    else:
        return "Tipo inválido. Usa 'hexa' o 'rgb'."

# Nivel 3

def shuffle_list(lista):
    lista_copy = lista[:]
    random.shuffle(lista_copy)
    return lista_copy

def unique_random_numbers():
    return random.sample(range(10), 7)