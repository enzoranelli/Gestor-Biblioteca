import random
import funcionesAuxiliares as f
import re 
#--------------VARIABLES DE INICIALIZACION Y CONSTANTES-----------------

generos = ('Novela contemporánea','Ciencia ficción','Fantasía','Terror','Misterio','Romance','Aventuras','Distopía','Realismo mágico','Otros')
encabezados = ('codigo', 'titulo', 'autor', 'stock', 'genero')
#----------------------------------------------------------------------
#-----------------------DATOS DE PRUEBA--------------------------------
libros = [
    {"codigo": "1", "titulo": "1984", "autor": "George Orwell", "anio": 1949, "genero": "Ciencia ficción"},
    {"codigo": "2", "titulo": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes", "anio": 1605, "genero": "Novela contemporánea"},
    {"codigo": "3", "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "anio": 1967, "genero": "Realismo mágico"},
    {"codigo": "4", "titulo": "La casa de los espíritus", "autor": "Isabel Allende", "anio": 1982, "genero": "Realismo mágico"},
    {"codigo": "5", "titulo": "La sombra del viento", "autor": "Carlos Ruiz Zafón", "anio": 2001, "genero": "Misterio"},
    {"codigo": "6", "titulo": "Ficciones", "autor": "Jorge Luis Borges", "anio": 1944, "genero": "Otros"},
    {"codigo": "7", "titulo": "Pedro Páramo", "autor": "Juan Rulfo", "anio": 1955, "genero": "Realismo mágico"},
    {"codigo": "8", "titulo": "El principito", "autor": "Antoine de Saint-Exupéry", "anio": 1943, "genero": "Fantasía"},
    {"codigo": "9", "titulo": "El túnel", "autor": "Ernesto Sabato", "anio": 1948, "genero": "Novela contemporánea"},
    {"codigo": "10", "titulo": "Rayuela", "autor": "Julio Cortázar", "anio": 1963, "genero": "Novela contemporánea"},
    {"codigo": "11", "titulo": "It (Eso)", "autor": "Stephen King", "anio": 1986, "genero": "Terror"},
    {"codigo": "12", "titulo": "El resplandor", "autor": "Stephen King", "anio": 1977, "genero": "Terror"},
    {"codigo": "13", "titulo": "Drácula", "autor": "Bram Stoker", "anio": 1897, "genero": "Terror"},
    {"codigo": "14", "titulo": "Frankenstein", "autor": "Mary Shelley", "anio": 1818, "genero": "Ciencia ficción"},
    {"codigo": "15", "titulo": "La llamada de Cthulhu", "autor": "H.P. Lovecraft", "anio": 1928, "genero": "Terror"},
    {"codigo": "16", "titulo": "El exorcista", "autor": "William Peter Blatty", "anio": 1971, "genero": "Terror"},
    {"codigo": "17", "titulo": "El juego de Gerald", "autor": "Stephen King", "anio": 1992, "genero": "Terror"},
    {"codigo": "18", "titulo": "La maldición de Hill House", "autor": "Shirley Jackson", "anio": 1959, "genero": "Terror"},
    {"codigo": "19", "titulo": "El Horla", "autor": "Guy de Maupassant", "anio": 1887, "genero": "Terror"},
    {"codigo": "20", "titulo": "La casa infernal", "autor": "Richard Matheson", "anio": 1971, "genero": "Terror"},
    {"codigo": "21", "titulo": "Los 7 hábitos de la gente altamente efectiva", "autor": "Stephen R. Covey", "anio": 1989, "genero": "Otros"},
    {"codigo": "22", "titulo": "Piense y hágase rico", "autor": "Napoleon Hill", "anio": 1937, "genero": "Otros"},
    {"codigo": "23", "titulo": "Cómo ganar amigos e influir sobre las personas", "autor": "Dale Carnegie", "anio": 1936, "genero": "Otros"},
    {"codigo": "24", "titulo": "El poder del ahora", "autor": "Eckhart Tolle", "anio": 1997, "genero": "Otros"},
    {"codigo": "25", "titulo": "Tus zonas erróneas", "autor": "Wayne Dyer", "anio": 1976, "genero": "Otros"},
    {"codigo": "26", "titulo": "Vivir la vida con sentido", "autor": "Viktor Frankl", "anio": 1946, "genero": "Otros"},
    {"codigo": "27", "titulo": "La magia del orden", "autor": "Marie Kondo", "anio": 2011, "genero": "Otros"},
    {"codigo": "28", "titulo": "Ámate a ti mismo como si tu vida dependiera de ello", "autor": "Kamal Ravikant", "anio": 2012, "genero": "Otros"},
    {"codigo": "29", "titulo": "Despierta tu héroe interior", "autor": "Victor Hugo Manzanilla", "anio": 2014, "genero": "Otros"},
    {"codigo": "30", "titulo": "Los secretos de la mente millonaria", "autor": "T. Harv Eker", "anio": 2005, "genero": "Otros"},
]
def incializarLibros():
    for i in range(len(libros)):
        libros[i]['stock'] = random.randint(0,20) #Harcelo lambda
    return libros
#----------------------------------------------------------------------


def imprimirSubMenu():
    '''
    Imprime el menu de opciones de libros
    Entrada: Vacio
    Salida: Vacio

    '''
    f.imprimirLinea(30)
    print("[1] Ver libros")
    print("[2] Agregar libro")
    print("[3] Buscar libro por título")
    print("[4] Buscar libro por autor")
    print("[5] Tabla de stock de libros")
    print("[6] Volver al menu principal")
    f.imprimirLinea(30)


def buscarLibroPorTitulo(listaLibros):
    '''
    Busca libros por título e imprime su información completa
    Entrada: lista de libros
    Salida: vacío
    '''
    tituloBuscar = input("Ingrese el título a buscar: ").lower()
    librosEncontrados = [libro for libro in listaLibros if tituloBuscar in libro['titulo'].lower()]
    if librosEncontrados:
        mostrarLibros(librosEncontrados)
    else:
        print("No se encontraron libros con ese título.")

def buscarLibroPorAutor(listaLibros):
    '''
    Busca libros por autor e imprime su información completa
    Entrada: lista de libros
    Salida: vacío
    '''
    autorBuscar = input("Ingrese el autor a buscar: ").lower()
    librosEncontrados = [libro for libro in listaLibros if autorBuscar in libro['autor'].lower()]
    if librosEncontrados:
        mostrarLibros(librosEncontrados)
    else:
        print("No se encontraron libros de ese autor.")
        

def agregarLibro(listaLibros):
    '''
    Solicita los datos para un nuevo libro
    Salida: diccionario con datos de libro

    '''
    print("Agregar Libro")
    #Validar titulo no este vacio
    titulo = input("Titulo: ").strip()
    while titulo == "":
        print("El título no puede estar vacío.")
        titulo = input("Titulo: ").strip()
    #Validar autor no este vacio ni contenga numeros
    autor = input("Autor: ").strip()
    while autor == "" or not esAutorValido(autor):
        print("El autor no puede estar vacío y debe contener solo letras (puede incluir tildes y espacios).")
        autor = input("Autor: ").strip()


    #Validar stock sea un numero positivo
    stock = -1
    while stock < 0:        
        try:
            stock = int(input("Stock: "))  
            if stock < 0:
                print("Debe ser un número positivo.")
        except ValueError:     
            print("Stock inválido, debe ser un número.")
 
 #Elegir genero y validar codigo unico
    genero = elegirGenero()
    codigo = -1
    verificarCodigo= True
    while codigo < 0 or verificarCodigo:     
        try:
            # codigo <0 or ~True
            codigo = int(input("Codigo: "))
            verificarCodigo = codigoExistente(codigo, listaLibros)
            if codigo < 0:
                print("El código debe ser un número positivo.")
        except ValueError:
            print("Codigo invalido, debe ser un numero")         
    return {"titulo": titulo, "autor": autor, "stock": stock, "codigo": codigo, "genero": genero}

def buscarLibroPorCodigo(codigo, listaLibros):
    '''
    Busca un libro por su codigo
    Entrada: codigo, listaLibros
    Salida: libro o -1 si no existe

    '''
    for libro in listaLibros:
        if libro['codigo'] == codigo:
            return libro
    return -1

def tituloDeLibroPorCodigo(codigo, listaLibros):
    '''
    Busca el titulo de un libro por su codigo
    Entrada: codigo, listaLibros
    Salida: titulo o -1 si no existe

    '''
    for libro in listaLibros:
        if libro['codigo'] == codigo:
            return libro['titulo']
    return -1
def indiceLibroPorCodigo(codigo, listaLibros):
    '''
    Busca el indice de un libro por su codigo
    Entrada: codigo, listaLibros
    Salida: indice o -1 si no existe

    '''
    for i in range(len(listaLibros)):
        if listaLibros[i]['codigo'] == codigo:
            return i
    return -1

def esAutorValido(autor):
    '''
    Verifica si el autor contiene solo letras (con tildes) y espacios
    '''
    patron = r'^[A-Za-zÁÉÍÓÚáéíóúÑñüÜ ]+$'
    return re.match(patron, autor) is not None

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
        try:
            opcion = int(input("Opcion: "))
            if 0 <= opcion < len(generos):
                return generos[opcion]
            else:
                print("Opcion invalida. Intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Debe ingresar un número entero.")
            opcion = -1
       
def tablaStockDeLibros(listaLibros):
    '''
    Muestra la tabla de stock de libros
    Entrada: lista de libros
    Salida: Vacio

    '''
    tabla = []
    conStock = []
    sinStock = []
    for libro in listaLibros:
        if libro['stock'] > 0:
            conStock.append(libro)
        else:
            sinStock.append(libro)

    tabla.append(conStock)
    tabla.append(sinStock)
    #encabezado = 'Titulo\tAutor\tStock'
    encabezado = f"{f.agregarEspacios(60,encabezados[1])} | {f.agregarEspacios(25,encabezados[2])} | {f.agregarEspacios(5,encabezados[3])}"
    
    print("\nLibros con stock:\n")
    print(encabezado)
    f.imprimirLinea(95)
    for i in range(len(tabla[0])):
        libro = tabla[0][i]
        print(f"{f.agregarEspacios(60,libro[encabezados[1]])} | {f.agregarEspacios(25,libro[encabezados[2]])} | {f.agregarEspacios(5,libro[encabezados[3]])}", end='\n')


    print("\nLibros sin stock:\n")
    print(encabezado)
    f.imprimirLinea(95)
    for i in range(len(tabla[1])):
        libro = tabla[1][i]
        print(f"{f.agregarEspacios(60,libro[encabezados[1]])} | {f.agregarEspacios(25,libro[encabezados[2]])} | {f.agregarEspacios(5,libro[encabezados[3]])}", end='\n')
            



def codigoExistente(codigo, listaLibros):
    '''
    Verifica si el codigo ya existe en la lista de libros 
    Entrada: codigo, lista de libros
    Salida: True si existe, False si no existe

    '''
    for libro in listaLibros:
        if libro['codigo'] == codigo:
            print("El código ya existe. Por favor, ingrese un código diferente.")
            return True
    return False

def mostrarLibros(listaLibros):
    '''
    Muestra los libros en formato de tabla usando alineación fija.
    Entrada: Vacio
    Salida: Vacio
    '''
    print("\nLista de Libros:")
    print(f"{f.agregarEspacios(6,encabezados[0])} | {f.agregarEspacios(60,encabezados[1])} | {f.agregarEspacios(25,encabezados[2])} | {f.agregarEspacios(5,encabezados[3])} | {encabezados[4]}")
    f.imprimirLinea(150)
    for libro in listaLibros:
        print(f"{f.agregarEspacios(6,libro[encabezados[0]])} | {f.agregarEspacios(60,libro[encabezados[1]])} | {f.agregarEspacios(25,libro[encabezados[2]])} | {f.agregarEspacios(5,libro[encabezados[3]])} | {libro[encabezados[4]]}")