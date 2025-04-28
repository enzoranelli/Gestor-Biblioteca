import libros
import usuarios
#--------------VARIABLES DE INICIALIZACION Y CONSTANTES-----------------

estadoPrestamo = ('devuelto', 'sin devolver')

#----------------------------------------------------------------------
def imprimirSubMenu():
    '''
    Imprime el menu de opciones de prestamos
    Entrada: Vacio
    Salida: Vacio

    '''
    print('---------------------------')
    print("[1] Agregar Prestamo")
    print("[2] Mostrar Prestamos")
    print("[3] Volver al menu principal")
    print('---------------------------')

def mostrarPrestamos(listaPrestamos):
    '''
    Muestra los prestamos en pantalla
    Entrada: lista de prestamos
    Salida: Vacio
    '''
    print("Lista de Prestamos:")
    for prestamo in listaPrestamos:
        print(f"DNI Usuario: {prestamo['dniUsuario']}, Codigo Libro: {prestamo['codigoLibro']}, Fecha Prestamo: {prestamo['fechaPrestamo']}, Fecha Devolucion: {prestamo['fechaDevolucion']}, Estado: {prestamo['estado']}")
    

def agregarPrestamo(listaUsuarios, listaLibros):
    '''
    Solicita los datos para un nuevo prestamo
    Salida: diccionario con datos de prestamo

    '''
    print("Agregar Prestamo")
    dniUsuario = input("DNI del usuario: ")
    while usuarios.buscarUsuarioPorDni(dniUsuario, listaUsuarios) == -1:
        print("DNI invalido o no existe")
        dniUsuario = input("DNI del usuario: ")
    
    codigoLibro = input("Codigo del libro: ")

    while libros.buscarLibroPorCodigo(codigoLibro, listaLibros) == -1:
        print("Codigo invalido o no existe")
        codigoLibro = input("Codigo del libro: ")
    libro = libros.buscarLibroPorCodigo(codigoLibro, listaLibros) 
    if(libro['stock'] <= 0):
        print("No hay stock disponible")
        return -1
    fechaPrestamo = input("Fecha de prestamo (dd/mm/aaaa): ")
    while verificarFecha(fechaPrestamo) == False:
        print("Fecha invalida")
        fechaPrestamo = input("Fecha de prestamo (dd/mm/aaaa): ")
    
    fechaDevolucion = input("Fecha de devolucion (dd/mm/aaaa): ")
    while verificarFecha(fechaDevolucion) == False:
        print("Fecha invalida")
        fechaDevolucion = input("Fecha de devolucion (dd/mm/aaaa): ")
    
    return {"dniUsuario": dniUsuario, "codigoLibro": codigoLibro, "fechaPrestamo": fechaPrestamo, "fechaDevolucion": fechaDevolucion, "estado": estadoPrestamo[1]}


def verificarFecha(fecha):
    '''
    Verifica si la fecha ingresada es valida
    Entrada: fecha
    Salida: True si es valida, False si no lo es

    '''
    dia, mes, anio = fecha.split('/')
    dia = int(dia)
    mes = int(mes)
    anio = int(anio) 
    diasPorMes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]	
    if anioBisiesto(anio):
        diasPorMes[1] = 29
    if mes > 0 and mes <=12 and dia > 0 and dia<= diasPorMes[mes-1]:
        return True
    else:
        print("Fecha invalida")
        return False

def anioBisiesto(anio):
    '''
    Verifica si el año es bisiesto
    Entrada: año
    Salida: True si es bisiesto, False si no lo es

    '''
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)
    
