import funcionesAuxiliares as f
import re
def imprimirSubMenu():
    '''
        Imprime el menu de opciones de usuarios
        Entrada: Vacio
        Salida: Vacio

    '''
    f.imprimirLinea(30)
    print('[1] Agregar Usuario')
    print('[2] Mostrar Usuarios')
    print('[3] Buscar usuarios por dominio de correo')
    print('[4] Volver al menu principal')
    f.imprimirLinea(30)

def obtenerUsuariosPorMail(dominioMail, listaUsuarios):
    '''
    Busca los usuarios por su dominio de correO
    Entrada: dominioMail, listaUsuarios
    Salida: lista de usuarios con el dominio de correo especificado

    '''
    usuariosPorMail = [usuario for usuario in listaUsuarios if usuario['correo'][-len(dominioMail):] == dominioMail]
   
    return usuariosPorMail
def indiceUsuarioPorDni(dni, listaUsuarios):
    '''
    Busca el indice de un usuario por su dni
    Entrada: dni, listaUsuarios
    Salida: indice del usuario o -1 si no existe

    '''
    for i in range(len(listaUsuarios)):
        if listaUsuarios[i]['dni'] == dni:
            return i
    return -1
def mostrarUsuarios(usuarios):
    '''
    Muestra los usuarios en pantalla
    Entrada: lista de usuarios
    Salida: Vacio

    '''

    print("\nLista de Usuarios:\n")
    print(f"{f.agregarEspacios(20,'Nombre')} | {f.agregarEspacios(5,'Edad')} | {f.agregarEspacios(30,'Correo')} | {'DNI'}")
    f.imprimirLinea(90)
    for usuario in usuarios:
        print(f"{f.agregarEspacios(20,usuario['nombre'])} | {f.agregarEspacios(5,usuario['edad'])} | {f.agregarEspacios(30,usuario['correo'])} | {usuario['dni']}")


def cagarDatosUsuario(usuarios):
    '''
    
    Solicita los datos para un nuevo usuario
    Salida: diccionario con datos de usuario

    '''

    print("Agregar Usuario")

    nombre = input("Nombre: ")
    while not validarNombre(nombre):
        print("Nombre invalido. Solo letras y espacios.")
        nombre = input("Nombre: ")

    edad = -1
    while edad <= 0 or edad > 109:
        try:
            edad = int(input("Edad: "))
            if edad <= 0:
                print("Debe ser un número positivo.")
            elif edad > 109:
                print ("Error, la edad debe ser menor a 110")  
        except ValueError:
            print("Edad invalida. Debe ser un numero entero.")
            edad = -1

    # Validar correo
    correo = input("Correo: ")
    while not validarCorreo(correo):
        print("Correo inválido. Debe contener '@' y '.' con un dominio válido.")
        correo = input("Correo: ")
    #Agregar try a DNI 
    dni = input("DNI: ").strip()
    while not validarDni(dni) or dniExistente(dni, usuarios):
        print("DNI invalido o ya existe, debe tener 8 digitos")
        dni = input("DNI: ").strip()
    return {"nombre": nombre, "edad": edad, "correo": correo, "dni": dni, "prestamos":[]}

def validarDni(dni):
    '''
    Valida el DNI ingresado por el usuario
    Entrada: dni
    Salida: True si es valido, False si no lo es

    '''

    return dni.isdigit() and len(dni) == 8

def validarCorreo(correo):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w{2,4}$'
    return re.match(patron, correo) is not None

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
       

def validarNombre(nombre):

    '''
    Valida que el nombre solo contenga letras y espacios
    Entrada: nombre
    Salida: True si es valido, False si no lo es

    '''
    if not nombre.strip():
        return False
    patron = r'^[A-Za-zÁÉÍÓÚáéíóúÑñ ]+$'

    return re.match(patron, nombre) is not None
   
