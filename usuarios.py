def imprimirSubMenu():
    '''
        Imprime el menu de opciones de usuarios
        Entrada: Vacio
        Salida: Vacio

    '''
    print('---------------------------')
    print("[1] Agregar Usuario")
    print("[2] Mostrar Usuarios")
    print("[3] Volver al menu principal")
    print('---------------------------')

def mostrarUsuarios(usuarios):
    '''
    Muestra los usuarios en pantalla
    Entrada: lista de usuarios
    Salida: Vacio

    '''
    print("Lista de Usuarios:")
    for usuario in usuarios:
        print(f"Nombre: {usuario['nombre']}, Edad: {usuario['edad']}, Correo: {usuario['correo']},DNI: {usuario['dni']}")


def agregarUsuario(usuarios):
    '''
    
    Solicita los datos para un nuevo usuario
    Salida: diccionario con datos de usuario

    '''

    print("Agregar Usuario")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    correo = input("Correo: ")
    dni = input("DNI: ")
    while not validarDni(dni) or dniExistente(dni, usuarios):
        print("DNI invalido o ya existe")
        print("DNI debe tener 8 digitos")
        dni = input("DNI: ")
    return {"nombre": nombre, "edad": edad, "correo": correo, "dni": dni, "prestamos":[]}

def validarDni(dni):
    '''
    Valida el DNI ingresado por el usuario
    Entrada: dni
    Salida: True si es valido, False si no lo es

    '''
    return len(dni) <= 8 or not dni.isdigit()


def buscarUsuarioPorDni(dni, listaUsuarios):
    '''
    Busca un usuario por su dni
    Entrada: dni, listaUsuarios
    Salida: usuario o -1 si no existe

    '''
    for usuario in listaUsuarios:
        if usuario['dni'] == dni:
            return usuario
    return -1

def dniExistente(dni, usuarios):
    '''
    Verifica si el DNI ya existe en la lista de usuarios
    Entrada: dni, lista de usuarios
    Salida: True si existe, False si no existe

    '''
    for usuario in usuarios:
        if usuario['dni'] == dni:
            return True
    return False
       