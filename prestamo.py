#--------------VARIABLES DE INICIALIZACION Y CONSTANTES-----------------

estadoPrestamo = ('devuelto', 'sin devolver')

#----------------------------------------------------------------------


def agregarPrestamo():
    '''
    Solicita los datos para un nuevo prestamo
    Salida: diccionario con datos de prestamo

    '''
    print("Agregar Prestamo")
    dniUsuario = input("DNI del usuario: ")
    codigoLibro = input("Codigo del libro: ")
    fechaPrestamo = input("Fecha de prestamo (dd/mm/aaaa): ")
    fechaDevolucion = input("Fecha de devolucion (dd/mm/aaaa): ")
    
    return {"dniUsuario": dniUsuario, "codigoLibro": codigoLibro, "fechaPrestamo": fechaPrestamo, "fechaDevolucion": fechaDevolucion, "estado": estadoPrestamo[1]}
def buscarLibroPorCodigo(codigo, listaLibros):
    '''
    Busca un libro por su codigo
    Entrada: codigo, listaLibros
    Salida: libro o None si no existe

    '''
    for libro in listaLibros:
        if libro['codigo'] == codigo:
            return libro
    return None
def buscarUsuarioPorDni(dni, listaUsuarios):
    '''
    Busca un usuario por su dni
    Entrada: dni, listaUsuarios
    Salida: usuario o None si no existe

    '''
    for usuario in listaUsuarios:
        if usuario['dni'] == dni:
            return usuario
    return None