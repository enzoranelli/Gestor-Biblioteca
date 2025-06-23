tupla = ('d',1,4)

print(tupla[1])

#COSAS A IMPLEMENTAR
#Opcion de busqueda de autor o libro que empiece por  "x" letra

#OPCION USAR LAMBDA
#Usar lambda + map: Mostrar lista resumida de préstamos
#En mostrarPrestamos de prestamos.py, podrías preparar una versión más "resumida" de préstamos para luego imprimirlos o guardarlos:

resumen = list(map(lambda p: f"{p['dniUsuario']} tiene el libro {p['codigoLibro']} hasta {p['fechaDevolucion']}", listaPrestamos))
for linea in resumen:
    print(linea)


#OPCION USAR REDUCE
#Podés usar reduce para contar cantidad total de libros en stock
#Esto requiere importar reduce:
from functools import reduce

#Y luego, por ejemplo en libros.py:
totalStock = reduce(lambda acc, libro: acc + libro['stock'], listaLibros, 0)
print("Stock total de libros:", totalStock)


def mostrarTitulosEnMayuscula(listaLibros):
    titulos = list(map(lambda libro: libro['titulo'].upper(), listaLibros))
    print("Títulos de libros en mayúscula:")
    for titulo in titulos:
        print("-", titulo)

#  1. Validar formato de correo electrónico (en usuarios.py)

import re

def validarCorreo(correo):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w{2,4}$'
    return re.match(patron, correo) is not None

#Uso en cagarDatosUsuario:
correo = input("Correo: ")
while not validarCorreo(correo):
    print("Correo inválido. Intente nuevamente.")
    correo = input("Correo: ")

#2. Validar que el nombre del usuario solo tenga letras y espacios

def validarNombre(nombre):
    patron = r'^[A-Za-zÁÉÍÓÚáéíóúÑñ ]+$'

    return re.match(patron, nombre) is not None
   
#Uso
nombre = input("Nombre: ")
while not validarNombre(nombre):
    print("Nombre inválido. Solo letras y espacios.")
    nombre = input("Nombre: ")

#Verificar campos obligatorios que no esten vacios


def mostrarCantidadPrestamosActivos(listaPrestamos):
    '''
    Muestra la cantidad de préstamos activos (no devueltos)
    Entrada: lista de préstamos
    Salida: None.
    '''

    pendientes = list(filter(lambda p: p['estado'] == 'sin devolver', listaPrestamos))
    cantidad = sum(1 for p in listaPrestamos if p['estado'] == 'sin devolver')
    print(f"\nActualmente hay {cantidad} préstamos activos.\n")








