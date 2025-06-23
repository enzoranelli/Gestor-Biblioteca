import libros
import usuarios
import funcionesAuxiliares as f
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
    print('[3] Cambiar estado de prestamo')
    print("[4] Volver al menu principal")
    print('---------------------------')

def mostrarPrestamos(listaPrestamos):
    '''
    Muestra los prestamos en pantalla
    Entrada: lista de prestamos
    Salida: Vacio
    '''
    print("Lista de Prestamos:")

    print(f"{f.agregarEspacios(10,"DNI")} | {f.agregarEspacios(10,"Código Libro")} | {f.agregarEspacios(15,"Fecha Préstamo")} | {f.agregarEspacios(15,"Fecha Devolución")} | {'Estado'}")
    f.imprimirLinea()
    for prestamo in listaPrestamos:
        print(f"{f.agregarEspacios(10,prestamo['dniUsuario'])} | {f.agregarEspacios(10,prestamo['codigoLibro'])} | {f.agregarEspacios(15,prestamo['fechaPrestamo'])} | {f.agregarEspacios(15,prestamo['fechaDevolucion'])} | {prestamo['estado']}")
    
def buscarPrestamoPorDni(dni, listaPrestamos):
    '''
    Busca indice de un prestamo por su dni
    Entrada: dni, listaPrestamos
    Salida: prestamo o -1 si no existe

    '''
    for i in range(len(listaPrestamos)):
        if listaPrestamos[i]['dniUsuario'] == dni and listaPrestamos[i]['estado'] == estadoPrestamo[1]:
            return i
    return -1

def cambiarEstadoPrestamo(indice, listaPrestamos):
    '''
    Cambia el estado de un prestamo
    Entrada: dni, listaPrestamos
    Salida: lista de prestamos

    '''

    prestamo = listaPrestamos[indice]

    prestamo['estado'] = estadoPrestamo[0]
    
    return prestamo
   
   
   

    
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
    libro = libros.buscarLibroPorCodigo(codigoLibro, listaLibros) 
    while libro == -1:
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
        return False

def anioBisiesto(anio):
    '''
    Verifica si el año es bisiesto
    Entrada: año
    Salida: True si es bisiesto, False si no lo es

    '''
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)
    
def gestionarDevolucion(listaPrestamos, listaUsuarios):
    '''
    Permite al usuario elegir cuál préstamo desea devolver si tiene varios pendientes
    Entrada: lista de préstamos y usuarios
    Salida: préstamo actualizado o None si no se devolvió ninguno
    '''
    dni = input("Ingrese el DNI del usuario: ")
    while usuarios.buscarUsuarioPorDni(dni, listaUsuarios) == -1:
        print("DNI inválido o no encontrado.")
        dni = input("Ingrese el DNI del usuario: ")

    prestamosPendientes = [p for p in listaPrestamos if p['dniUsuario'] == dni and p['estado'] == estadoPrestamo[1]]

    if len(prestamosPendientes) == 0:
        print("El usuario no tiene préstamos pendientes.")
        return None

    print("\nPréstamos sin devolver:")
    print(f"{f.agregarEspacios(8,"Opción")} | {f.agregarEspacios(12,'DNI Usuario')} | {f.agregarEspacios(14,'Código Libro')} | {f.agregarEspacios(18,'Fecha Préstamo')} | {f.agregarEspacios(18,'Fecha Devolución')} | {'Estado'}")
    f.imprimirLinea(90)
    for i, p in enumerate(prestamosPendientes):
        print(f"[{i+1}]{f.agregarEspacios(3,'')} | {f.agregarEspacios(12,p['dniUsuario'])} | {f.agregarEspacios(14,p['codigoLibro'])} | {f.agregarEspacios(18,p['fechaPrestamo'])} | {f.agregarEspacios(18,p['fechaDevolucion'])} | {p['estado']}")

    opcion = input("Seleccione el número del préstamo que desea marcar como devuelto: ")
 
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > len(prestamosPendientes):
        print("Opción inválida.")
        opcion = input("Seleccione el número del préstamo que desea marcar como devuelto: ")

    opcion = int(opcion)
    prestamoSeleccionado = prestamosPendientes[opcion - 1]
    prestamoSeleccionado['estado'] = estadoPrestamo[0]
    print("Préstamo actualizado como 'devuelto'.")

    return prestamoSeleccionado