import libros
libros = []
'''
. Estructurar el MAIN, inicializacion de  variables
· Añadir libros al inventario

· Registrar nuevos usuarios 

· Buscar libros por título, autor o año

· Prestar y devolver libros

· Ver libros disponibles

· Mostrar usuarios y sus préstamos
'''
libros.inicializarLibros()

'''
Tuplas:
Categorias
fechas, dni, codigo libro

lista[-3::4]

f

Listas de diccionarios:
libros = [ libro, libro, ...]
usuarios = [ usuario, ...]
prestamos = [ prestamo, ...]

Diccionarios:
libro = {
    titulo : El principito,
    autor,
    categoria,
    anio,
    stock,
    codigo

}


for i in range( len(lista)):

    lista[]
genero = 
usuario = {
    nombre,
    dni,
    prestamos : [lista de prestamos]
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
        IMPRIME EL MENU
    
    
    '''
    print('---------------------------')
    print('Opciones: \n[1]Agregar libro\n[2]Ver inventario de libros')
    print('[0]Para salir')
    print('---------------------------')


salir = 1
while salir !=0:
    imprimirMenu()
    opcion = int(input('Escribir opcion: '))
    if opcion == 0:
        salir = 0 
    elif opcion == 1:
        libros.libro_print()
    else:
        print('Opcion invalida.')