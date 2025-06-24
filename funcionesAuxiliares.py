import json
def agregarEspacios(cantidad,texto):
    '''
        Agrega los espacios necesarios a un texto para que tenga un largo especificado.
        Entrada: cantidad(int), texto(str)
        Salida: texto con espacios agregados, si es necesario, o el texto original si es mayor o igual a la cantidad.
    '''

    if len(str(texto)) < cantidad:
        return  str(texto) + " " * (cantidad - len(str(texto))) 
    else:
        return texto
    
def imprimirLinea(cantidad):
    '''
        Imprime una linea de guiones con la cantidad especificada.
        Entrada: cantidad(int)
        Salida: Vacio
    '''
    print("-"*cantidad)

def inicializarDatos(nombreArchivo):
    '''
        Inicializa los datos de un archivo JSON.
        Entrada: nombreArchivo(str)
        Salida: lista de datos cargados del archivo o una lista vacia si el archivo no existe.
    '''
    try:
        with open('./datos/'+nombreArchivo, 'r', encoding='UTF-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"El archivo {nombreArchivo} no existe. Se creará una lista vacía.")
        return []  
    except PermissionError:
        print(f"Sin permiso para leer el archivo {nombreArchivo}. Se creará una lista vacía.")
        return []  
    except Exception as e:
        print(f"Error inesperado al leer el archivo {nombreArchivo}: {e}. Se creará una lista vacía.")
        return []
    
def actualizarDatos(nombreArchivo, listaDatos):
    '''
        Actualiza los datos de un archivo JSON.
        Entrada: nombreArchivo(str), listaDatos(list)
        Salida: Vacio
    '''
    try:
        with open('./datos/'+nombreArchivo, 'w', encoding='UTF-8') as archivo:
            archivo.write(json.dumps(listaDatos, indent=4))
    except Exception as e:
        print(f"Error al actualizar el archivo {nombreArchivo}: {e}")
        
def fechaVencida(fechaDevolucion, fechaActual):
    '''
        Verifica si una fecha de devolución está vencida en comparación con la fecha actual.
        Entrada: fechaDevolucion(str) en formato 'DD/MM/AAAA', fechaActual(str) en formato 'DD/MM/AAAA'
        Salida: True si la fecha de devolución es anterior a la fecha actual, False en caso contrario.
    '''
    diaDev, mesDev, anioDev = map(int, fechaDevolucion.split('/'))
    diaAct, mesAct, anioAct = map(int, fechaActual.split('/'))
    if anioDev < anioAct:
        return True
    elif anioDev == anioAct:
        if mesDev < mesAct:
            return True
        elif mesDev == mesAct:
            return diaDev < diaAct

def registrarExcepcion(e, lugar):
    try:
        archivo = open('errores.log','a')
        try:
            error = f"Tipo de error: {type(e)} - Mensaje:{str(e)} - Lugar: {lugar}\n"
            archivo.write(error)
        finally:
            archivo.close()
    except Exception as logError:
        print(f"Error al escribir en el log: {logError}")
