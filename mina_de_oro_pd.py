#Problema Mina de Oro con Dinamica
#Kevin Rodriguez - Josue Rodriguez
#Investigacion de Operacion
#TEC

import time
import argparse
global matrizDeCantidad
global filas
global columnas
global solucion

#Funcion main
def iniciarDinamica(minaDeOro,iteraciones):
    #Variables globales
    global filas
    global columnas
    global matrizDeCantidad
    global solucion
    #Ejemplos
    #minaDeOro = [[1,3,3],[2,1,4],[0,6,4]]
    #minaDeOro = [[10, 33, 13, 15],[22, 21, 0, 1],[5, 0, 2, 3],[0, 6, 14, 2]]
    #minaDeOro = [[1, 3, 1, 5],[2, 2, 4, 1],[5, 0, 2, 3],[0, 6, 1, 2]]

    #Largo filas
    filas = len(minaDeOro)
    #Largo columnas
    columnas = len(minaDeOro[0])
    #Llena la matriz de pesos/cantidades de 0
    llenarMatrizCantidad(filas,columnas)
    #Inicia el tiempo
    start_time = time.time()
    duracionFinal = 0
    i = 0
    #Hace el experimente n cantidad de veces y saca la duracion final
    while i < iteraciones:
        start_time = time.time()
        solucion  = solucionDinamica(minaDeOro,filas,columnas)
        print(solucion)
        duracion = time.time() - start_time
        duracionFinal += duracion
        print("Duracion: " + str(time.time() - start_time))
        i = i + 1
        llenarMatrizCantidad(filas,columnas)
    #Guarda en el indice 0 la duracion y en el indice 1 la respuesta
    respuestas = []
    respuestas.append(duracionFinal)
    respuestas.append(solucion)
    #Retorna las respuestas
    return respuestas

def solucionDinamica(minaDeOro,filas,columnas):
    global solucion
    #Numero de columnas inicial (Empieza el recorrido de la esquina mas a la derecha arriba)
    j = columnas - 1
    i = 0

    #Saca la solucion inicial para poder empezar hacer las comparaciones
    solucionAuxiliar = solucionDinamica2(minaDeOro,0,j)
    while i < filas:
        #Compara la solucion obtenido anterior con la obtenida actual y verifica cual es el maximo
        solucionAuxiliar2 = max(solucionAuxiliar,solucionDinamica2(minaDeOro,i+1,j))
        #Establece el nuevo maximo
        solucionAuxiliar = solucionAuxiliar2
        #Aumenta la fila
        i = i + 1
        #Si la fila llega al limite, se empieza a recorrer la siguiente columna y se vuelve a poner la fila en 0
        if(i == filas):
            j = j - 1
            i = 0
        #Si la columna llega a ser menor que 0, significa que ya termino de recorrer todas las columnas
        if (j < 0):
            break
    #print(matrizDeCantidad)
    solucion = solucionAuxiliar
    #Retorna el maximo obtenido
    return solucionAuxiliar

def solucionDinamica2(minaDeOro,i,j):
    global filas
    global columnas
    #Si se sale de los limites, retorno 0 .
    if i < 0 or i > filas-1 or j == columnas:
        return 0
    #Si ya se itero sobre el elemento, con fuerza bruta no tiene este "memoize"
    if matrizDeCantidad[i][j] != 0:
        return matrizDeCantidad[i][j]
    #Solucion si se mueve a la derecha
    derecha = solucionDinamica2(minaDeOro,i, j + 1)
    #Solucion si se mueve a la derecha arriba
    derechaArriba = solucionDinamica2(minaDeOro,i - 1, j + 1)
    #Solucion si se mueve a la derecha abajo
    derechaAbajo = solucionDinamica2(minaDeOro,i + 1, j + 1)
    #A la matriz de cantidad le asigna el valor de la mina de oro mas el maximo de los caminos posibles
    matrizDeCantidad[i][j] = minaDeOro[i][j] + max(derecha,derechaArriba,derechaAbajo)
    #Retorna el nuevo valor
    return matrizDeCantidad[i][j]



#Funcion que se encarga de llenar la matriz auxiliar con 0's
def llenarMatrizCantidad(filas,columnas):
    global matrizDeCantidad
    #Llena n cantidad de filas con 0
    matrizDeCantidad = [0] * filas
    for i in range(filas):
        #Llena n cantidad de columnas con 0
        matrizDeCantidad[i] = [0] * columnas


#Funcion que se encarga de leer el archivo de entrada
def leerArchivoEntrada(archivoEntrada):
    listaEntrada = []
    try:
        archivo = open(archivoEntrada,"r")
    except(FileNotFoundError):
        print("ERROR: Archivo de entrada no encontrado")
        exit(0)
    #Recorremos el archivo
    for linea in archivo:
        line = []
        line.append(linea.rstrip('\n'))
        listaEntrada.append(line)

    return listaEntrada

#Convierta la matriz a int para poder empezar a solucionarla
def convertirInt(matriz):
    lista = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            x = str(matriz[i][0])
            linea = x.split(",")
            lista2 = []
            for z in range(len(linea)):
                lista2.append(int(linea[z]))
            lista.append(lista2)

    return lista


#Main cuando se corre el archivo solo, agarra el nombre del archivo como argumentos
#Lee el archivoEntrada y lo convierte a Investigacion
#Llena la matriz auxiliar de 0 y empieza buscar la solucion
def main():
    global filas
    global columnas
    archivo = ""
    parser = argparse.ArgumentParser(description="Programa Mina de Oro Programacion Dinamica| Menu de Ayuda")
    #Crea o agrega los parametros. Siendo entrada obligatoria siempre. -o Opcional y salida siendo obligatoria si se pone -o
    parser.add_argument("-a",dest = "archivo", help = "Archivo de entrada")
    #Parseo los parametros o argumentos y guardo
    args = parser.parse_args()
    #Si encuentra argumento filas
    if args.archivo:
        archivo = args.archivo

    matriz = leerArchivoEntrada(archivo)
    mina = convertirInt(matriz)

    #Largo filas
    filas = len(mina)
    #Largo columnas
    columnas = len(mina[0])
    start_time = time.time()
    llenarMatrizCantidad(filas,columnas)
    print("La cantidad maxima de oro es: " + str(solucionDinamica(mina,filas,columnas)))
    print("Duracion con programacion dinamica: " + str(time.time() - start_time))

if __name__ == '__main__':
    main()
