#--------------VARIABLES DE INICIALIZACION Y CONSTANTES-----------------

generos = ('Novela contemporánea','Ciencia ficción','Fantasía','Terror','Misterio','Romance','Aventuras','Distopía','Realismo mágico','Otros')

#----------------------------------------------------------------------

def imprimirSubMenu():
    '''
    Imprime el menu de opciones de libros
    Entrada: Vacio
    Salida: Vacio

    '''
    print('---------------------------')
    print("[1] Ver libros")
    print("[2] Agregar libro")
    print("[3] Volver al menu principal")
    print('---------------------------')

def agregarLibro(listaLibros):
    '''
    Solicita los datos para un nuevo libro
    Salida: diccionario con datos de libro

    '''
    print("Agregar Libro")
    titulo = input("Titulo: ")
    autor = input("Autor: ")
    stock = int(input("Stock: "))
    genero = elegirGenero()
    codigo = input("Codigo: ")
    
    while codigoExistente(codigo, listaLibros):
        print("Codigo invalido, ya existe")
        codigo = input("Codigo: ")
    
    return {"titulo": titulo, "autor": autor, "stock": stock, "codigo": codigo, "genero": genero}

def elegirGenero():
    '''
    Solicita al usuario que elija un genero de libro
    Entrada: Vacio
    Salida: genero elegido

    '''
    print("Seleccione un genero:")
    for i, genero in enumerate(generos):
        print(f"[{i}] {genero}")
    opcion = -1
    while opcion < len(generos) or opcion > len(generos):
        opcion = int(input("Opcion: "))
        if 0 <= opcion < len(generos):
            return generos[opcion]
        else:
            print("Opcion invalida. Intente nuevamente.")
       

def codigoExistente(codigo, listaLibros):
    '''
    Verifica si el codigo ya existe en la lista de libros
    Entrada: codigo, lista de libros
    Salida: True si existe, False si no existe

    '''
    for libro in listaLibros:
        if libro['codigo'] == codigo:
            return True
    return False

def mostrarLibros(listaLibros):
    '''
    Muestra los libros en pantalla
    Entrada: Vacio
    Salida: Vacio

    '''
    print("Lista de Libros:")
    for libro in listaLibros:
        print(f"Titulo: {libro['titulo']}, Autor: {libro['autor']}, Stock: {libro['stock']}, Codigo: {libro['codigo']}, Genero: {libro['genero']}")