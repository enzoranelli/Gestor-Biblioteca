import libros
import usuarios
import prestamos
import funcionesAuxiliares as f
#--------------VARIABLES DE INICIALIZACION Y CONSTANTES-----------------

listaLibros = libros.incializarLibros()
listaPrestamos = []
listaUsuarios = []

#----------------------------------------------------------------------

def imprimirMenu():
    '''
        Imprime el menu principal
        Entrada: Vacio
        Salida: Vacio
    '''
    f.imprimirLinea(30)
    print('Opciones: \n[1]Panel libros\n[2]Panel usuarios\n[3]Panel prestamos')
    print('[0]Para salir')
    f.imprimirLinea(30)

#INICIO DEL PROGRAMA
salir = 1
while salir !=0:
    imprimirMenu()
    try:
        opcion = int(input('Escribir opcion: '))
        opcionSubMenu = 0
        if opcion == 0:
            salir = 0 
        elif opcion == 1:
            #Submenu de libros
            while opcionSubMenu != 6:
                libros.imprimirSubMenu()
                opcionSubMenu = int(input('Escribir opcion: '))
                if opcionSubMenu == 1:
                    libros.mostrarLibros(listaLibros)
                elif opcionSubMenu == 2:
                    listaLibros.append(libros.agregarLibro(listaLibros))
                    print('Libro agregado\n')
                elif opcionSubMenu == 3:
                    libros.buscarLibroPorTitulo(listaLibros)
                elif opcionSubMenu == 4:
                    libros.buscarLibroPorAutor(listaLibros)
                elif opcionSubMenu == 5:
                    libros.tablaStockDeLibros(listaLibros)
                    print('Tabla de stock de libros')
                elif opcionSubMenu == 6:
                    print('Volviendo al menu principal...')
                else:
                    print('Opcion invalida.')
        elif opcion == 2:
            #Submenu de usuarios
            while opcionSubMenu != 4:
                usuarios.imprimirSubMenu()
                opcionSubMenu = int(input('Escribir opcion: '))
                if opcionSubMenu == 1:
                    listaUsuarios.append(usuarios.cagarDatosUsuario(listaUsuarios))
                    print('Usuario agregado\n')
                elif opcionSubMenu == 2:
                    if len(listaUsuarios) > 0:
                        usuarios.mostrarUsuarios(listaUsuarios)
                    else:
                        print('No hay usuarios para mostrar')
                elif opcionSubMenu == 3:
                    dominioMail = input('Escribir dominio de correo: (ej: @hotmail.com): ')
                    usuariosPorMail = usuarios.obtenerUsuariosPorMail(dominioMail, listaUsuarios)
                    if len(usuariosPorMail) > 0:
                        print('Usuarios encontrados:')
                        usuarios.mostrarUsuarios(usuariosPorMail)
                    else:
                        print('No se encontraron usuarios con ese dominio de correo')
                elif opcionSubMenu == 4:
                    print('Volviendo al menu principal...')
                else:
                    print('Opcion invalida.')
        elif opcion == 3:
            #Submenu de prestamos
            while opcionSubMenu != 4:
                prestamos.imprimirSubMenu()
                opcionSubMenu = int(input('Escribir opcion: '))
                if opcionSubMenu == 1:
                    prestamo = prestamos.agregarPrestamo(listaUsuarios, listaLibros)
                    if prestamo != -1:
                        listaPrestamos.append(prestamo)
                        # Actualizar stock del libro
                        libro = libros.buscarLibroPorCodigo(prestamo['codigoLibro'], listaLibros)
                        if libro != -1:
                            if libro in listaLibros:
                                libro['stock'] -= 1
                                print(f'Stock actualizado: {libro["stock"]}')
                        else:
                            print('Libro no encontrado')
                        # Agregar prestamo al usuario"
                        usuario  = usuarios.buscarUsuarioPorDni(prestamo['dniUsuario'], listaUsuarios)
                        if usuario != -1:
                            usuario['prestamos'].append(prestamo)
                        else:
                            print('Usuario no encontrado')
                        print('Prestamo agregado\n')
                    else:
                        print('No se pudo agregar el prestamo')
                elif opcionSubMenu == 2:
                    if len(listaPrestamos) > 0:
                        prestamos.mostrarPrestamos(listaPrestamos)
                    else:
                        print('No hay prestamos para mostrar')
                    
                elif opcionSubMenu == 3:
                    # Cambiar estado de prestamo segun dni y estado de prestamo
                    print('Cambiar estado de prestamo')

                    prestamoDevuelto = prestamos.gestionarDevolucion(listaPrestamos, listaUsuarios)
                    if prestamoDevuelto:
                        indiceLibro = libros.indiceLibroPorCodigo(prestamoDevuelto['codigoLibro'], listaLibros)
                        if indiceLibro != -1:
                            listaLibros[indiceLibro]['stock'] += 1
                            print(f'Stock actualizado: {listaLibros[indiceLibro]["stock"]}')
                        else:
                            print("No se encontró el libro para actualizar stock.")
                elif opcionSubMenu == 4:
                    print('Volviendo al menu principal...') 
        else:
            print('Opcion invalida.')
    except ValueError:
        print('Error: Debe ingresar un numero entero.')