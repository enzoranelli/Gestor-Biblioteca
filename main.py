import libros
import usuarios

#--------------VARIABLES DE INICIALIZACION Y CONSTANTES-----------------

listaLibros = []
listaPrestamos = []
listaUsuarios = []

#----------------------------------------------------------------------


'''
. Estructurar el MAIN, inicializacion de  variables
· Añadir libros al inventario

· Registrar nuevos usuarios 

· Buscar libros por título, autor o año

· Prestar y devolver libros

· Ver libros disponibles

· Mostrar usuarios y sus préstamos
'''

'''
Tuplas:
Categorias
fechas

Listas de diccionarios:
libros = [ libro, libro, ...]
usuarios = [ usuario, ...]
prestamos = [ prestamo, ...]

Diccionarios:
libro = {
    titulo : El principito,
    autor,
    categoria,
    stock,
    codigo
}


for i in range( len(lista)):

    lista[]
genero = 
usuario = {
    nombre,
    dni,
    prestamos : [matriz de prestamos]
}

prestamos = {
    dniUsuario,
    codigoLibro,
    fechaPrestamo,
    fechaDevolucion,
    estado : (devuelto, sin devolver)
}
'''

def imprimirMenu():
    '''
        Imprime el menu principal
        Entrada: Vacio
        Salida: Vacio
    '''
    print('---------------------------')
    print('Opciones: \n[1]Panel libros\n[2]Panel usuarios\n[3]Panel prestamos')
    print('[0]Para salir')
    print('---------------------------')

#INICIO DEL PROGRAMA
salir = 1
while salir !=0:
    imprimirMenu()
    opcion = int(input('Escribir opcion: '))
    opcionSubMenu = 0
    if opcion == 0:
        salir = 0 
    elif opcion == 1:
        #Submenu de libros
        while opcionSubMenu != 3:
            libros.imprimirSubMenu()
            opcionSubMenu = int(input('Escribir opcion: '))
            if opcionSubMenu == 1:
                libros.mostrarLibros(listaLibros)
            elif opcionSubMenu == 2:
                listaLibros.append(libros.agregarLibro(listaLibros))
                print('Libro agregado\n')
            elif opcionSubMenu == 3:
                print('Volviendo al menu principal...')
            else:
                print('Opcion invalida.')
    elif opcion == 2:
        #Submenu de usuarios
        while opcionSubMenu != 3:
            usuarios.imprimirSubMenu()
            opcionSubMenu = int(input('Escribir opcion: '))
            if opcionSubMenu == 1:
                listaUsuarios.append(usuarios.agregarUsuario(listaUsuarios))
                print('Usuario agregado\n')
            elif opcionSubMenu == 2:
                usuarios.mostrarUsuarios(listaUsuarios)
            elif opcionSubMenu == 3:
                print('Volviendo al menu principal...')
            else:
                print('Opcion invalida.')
    
    else:
        print('Opcion invalida.')