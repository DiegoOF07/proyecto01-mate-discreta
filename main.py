import set_operations as so

users_sets = {}

def main():
    menu = True
    while menu:
        print('\n---CONJUNTOS---')
        print('1. Construir un nuevo conjunto')
        print('2. Operar conjuntos')
        print('3. Finalizar')
        selected = input('Seleccione una opción: ')

        try:
            op = int(selected)
            if op == 1: 
                create_set()

            if op == 2:
                perform_set_operations()
                        
            if op == 3:
                menu = False
        
        except ValueError:
            print('Por favor introduzca un número entre 1 y 3')

def create_set():
    print('\n---CONSTRUCCIÓN DE CONJUNTOS---')
    new_set = True
    new_set_elements = []

    while new_set:
        print(f'Sea \033[96mU = {so.UNIVERSAL_SET}')
        new_element = input(f'\033[0mIntroduzca un nuevo elemento: ')

        if new_element not in so.ALL_ELEMENTS or new_element == '':
            print('Por favor introduzca un elemento perteneciente a U')

        else:
            new_set_elements.append(new_element)

            keep_adding_validated = False
            while not keep_adding_validated:

                keep_adding = input('¿Desea agregar más elementos?(\033[92mS\033[0m/\033[91mN\033[0m): ')
                if keep_adding.upper() == 'S':
                    keep_adding_validated = True
                elif keep_adding.upper() == 'N':
                    keep_adding_validated = True
                    new_set = False
                else:
                    print('Seleccione una opción válida (S/N)')
    
    name_validated = False
    while not name_validated:
        new_set_name = input('¿Cómo desea llamar al conjunto?: ')
        if users_sets.get(new_set_name) is None:
            users_sets[new_set_name] = new_set_elements
            print(f'Conjunto \033[92m{new_set_name} = {set(new_set_elements)} \033[0mCreado exitosamente')
            name_validated = True
        else:
            print('\033[93mYa existe un conjunto con ese nombre\033[0m')

def perform_set_operations():
    if len(users_sets) < 2:
        print('\033[93mNo hay conjuntos suficientes para realizar operaciones. Debe construir al menos dos conjuntos\033[0m')
    else:
        print('\n---CONJUNTOS DEL USUARIO---')
        for k, v in users_sets.items():
            print(f'\033[94m{k} = {set(v)}\033[0m')

        first_set = input('\nPrimer conjunto en la operación: ')
        if first_set not in users_sets.keys():
            print('No existe un conjunto con ese nombre')
        
        second_set = input('Segundo conjunto en la operación: ')
        if second_set not in users_sets.keys():
            print('No existe un conjunto con ese nombre')

        operations_menu = True
        while operations_menu:
            print('\n---OPERACIONES ENTRE CONJUNTOS---')
            print('1. Complemento')
            print('2. Unión')
            print('3. Intersección')
            print('4. Diferencia')
            print('5. Diferencia Simétrica')
            print('6. Menú principal')
            operator = input('Seleccione una operación: ')

            try:
                op = int(operator)

                if op == 1:
                    print(f'\033[92m{first_set}\' = {so.get_complement(users_sets[first_set])}\033[0m')
                    print(f'\033[92m{second_set}\' = {so.get_complement(users_sets[second_set])}\033[0m')

                if op == 2:
                    union = so.set_union(users_sets[first_set], users_sets[second_set])
                    if len(union) == 0:
                        print(f'\033[92m{first_set} \u222A {second_set} = {'{ }'}\033[0m')
                    else:
                        print(f'\033[92m{first_set} \u222A {second_set} = {union}\033[0m')
                
                if op == 3:
                    intersection = so.set_intersection(users_sets[first_set], users_sets[second_set])
                    if len(intersection) == 0:
                        print(f'\033[92m{first_set} \u2229 {second_set} = {'{ }'}\033[0m')
                    else:
                        print(f'\033[92m{first_set} \u2229 {second_set} = {intersection}\033[0m')
                
                if op == 4:
                    diference = so.set_diference(users_sets[first_set], users_sets[second_set])
                    if len(diference) == 0:
                        print(f'\033[92m{first_set} - {second_set} = {'{ }'}\033[0m')
                    else:
                        print(f'\033[92m{first_set} - {second_set} = {diference}\033[0m')

                if op == 5:
                    simetric_diference = so.set_simetric_diference(users_sets[first_set], users_sets[second_set])
                    if len(simetric_diference) == 0:
                        print(f'\033[92m{first_set} \u2206 {second_set} = {'{ }'}\033[0m')
                    else:
                        print(f'\033[92m{first_set} \u2206 {second_set} = {simetric_diference}\033[0m')

                if op == 6:
                    operations_menu = False
                
            except ValueError:
                print('Por favor introduzca un número entre 1 y 6')

if __name__ == '__main__':
    main()