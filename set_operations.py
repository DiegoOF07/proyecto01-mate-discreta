# Diego Oswaldo Flores Rivas - 23714
# Nils Muralles Morales - 23727
# Módulo que contiene la generación y operaciones entre conjuntos

ALL_ELEMENTS = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
UNIVERSAL_SET = {ALL_ELEMENTS} # Conjunto Universal

# Método que devuelve la representación como una cadena de bits dado un arreglo con los elementos que el usuario desea incluir en un conjunto.
def generate_bit_string(users_input):
    bit_string = '' # Cadena inicializada
    universal_set_elements = ALL_ELEMENTS # Elementos del conjunto universal como un iterable ordenado

    # Si el elemento se encuentra en el input del usuario se agrega un 1 a la cadena
    for element in universal_set_elements:
        if element in users_input:
            bit_string += '1'
        else:
            bit_string += '0'

    return bit_string

# Método que devuelve un conjunto dada su representación como cadena de bits.
def generate_set(bit_string):
    output_set = set() # Conjunto de salida inicializado.
    universal_set_elements = ALL_ELEMENTS

    # Por cada uno en la representación como cadena de bits se agrega al conjunto que se retorna al usuario
    for i in range(len(universal_set_elements)):
        if bit_string[i] == '1':
            output_set.add(universal_set_elements[i])

    return output_set

# Método que realiza la unión entre dos conjuntos dados A y B.
def set_union(A, B):
    bit_string_a = generate_bit_string(A) # Representación como cadena de bits del conjunto A
    bit_string_b = generate_bit_string(B) # Representación como cadena de bits del conjunto B

    result = int(bit_string_a, 2) | int(bit_string_b, 2) # Unión como suma booleana de números binarios (OR)
    union_set_bit_string = bin(result)[2:].zfill(len(bit_string_a))

    return generate_set(union_set_bit_string)

# Método que realiza la intersección entre dos conjuntos dados A y B
def set_intersection(A, B):
    bit_string_a = generate_bit_string(A) # Representación como cadena de bits del conjunto A
    bit_string_b = generate_bit_string(B) # Representación como cadena de bits del conjunto B

    result = int(bit_string_a, 2) & int(bit_string_b, 2)
    intersection_set_bit_string = bin(result)[2:].zfill(len(bit_string_a))

    return generate_set(intersection_set_bit_string)

# Método que realiza la diferencia entre dos conjuntos dados A y B
def set_diference(A, B):
    bit_string_a = generate_bit_string(A) # Representación como cadena de bits del conjunto A
    bit_string_ab = generate_bit_string(set_intersection(A,B)) # Representación como cadena de bits del conjunto A intersección B

    result = int(bit_string_a, 2) - int(bit_string_ab, 2)
    diference_set_bit_string = bin(result)[2:].zfill(len(bit_string_a))

    return generate_set(diference_set_bit_string)

# Método que obtiene el complemento de un conjunto dado A
def get_complement(A):
    bit_string_a = generate_bit_string(A) # Representación como cadena de bits del conjunto A
    bit_string_u = generate_bit_string(ALL_ELEMENTS) # Representación como cadena de bits del conjunto U

    result = int(bit_string_u, 2) - int(bit_string_a, 2)
    complement_bit_string = bin(result)[2:].zfill(len(bit_string_a))
    
    return generate_set(complement_bit_string)

# Método que obtiene la diferencia entre dos conjuntos dados A, B
def set_simetric_diference(A, B):
    union_ab = set_union(A, B) # A U B
    intersection_ab = set_intersection(A, B) # A n B
    return set_diference(union_ab, intersection_ab) # (A U B) - (A n B)