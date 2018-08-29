#Problema Mina de Oro con Dinamica
#Kevin Rodriguez - Josue Rodriguez
#Investigacion de Operacion
#TEC

import random
import time
import argparse
from mina_de_oro_pd import *
from mina_de_oro_fb import *

global filas
global columnas
global iteraciones

def main():
    global filas
    global columnas
    parser = argparse.ArgumentParser(description="Programa Mina de Oro | Menu de Ayuda")

    #Crea o agrega los parametros. Siendo entrada obligatoria siempre. -o Opcional y salida siendo obligatoria si se pone -o
    parser.add_argument("-f",dest = "filas", help = "Cantidad de filas")
    parser.add_argument("-c", dest = "columnas", help = "Cantidad de columnas")
    parser.add_argument("-i", dest = "iteraciones", help = "Cantidad de iteraciones")

    #Parseo los parametros o argumentos y guardo
    args = parser.parse_args()

    #Si encuentra argumento filas
    if args.filas:
        filas = int(args.filas)
    #Si encuentra argumento columnas
    if args.columnas:
        columnas = int(args.columnas)
    if args.iteraciones:
        iteraciones = int(args.iteraciones)
    matriz = generar_Matriz() #Se genera la matriz
    print(matriz)
    print(filas)
    print(columnas)

    resp1 = iniciarFuerzaBruta(matriz,iteraciones) #Guarda los resultados de FB (tiempo,resultado)
    resp2 = iniciarDinamica(matriz,iteraciones)#Guarda los resultados de PD (tiempo,resultado)

    promedioFuerzaBruta = resp1[0] / iteraciones #Saca el promedio
    promedioDinamica = resp2[0] / iteraciones   #Saca el promedio


    print("Generando Reporte...")
    time.sleep(3)

    #Genera reporte
    generarReporteExperimento(filas,columnas,matriz,promedioFuerzaBruta,resp1[1],promedioDinamica,resp2[1],iteraciones)


#Se genera la matriz con numeros random hasta el 100
def generar_Matriz():
    matriz = []
    for i in range(0, filas):
        lista = []
        for j in range(0, columnas):
            lista.append(random.randrange(100))
        matriz.append(lista)
    return matriz

#Funcion que se encarga de escribir en un archivo el experimento realizado
def generarReporteExperimento(filas,columnas,mina,promedioFB,resFB,promedioPD,resPD,iteraciones):
    archivo = open("experimento_mina_oro.txt","w")
    archivo.write("Experimento con problema de Mina de Oro \n")
    archivo.write("Se eligieron " + str(filas) + " filas y " + str(columnas) + " columnas\n")
    archivo.write("Cantidad de iteraciones: " + str(iteraciones) + "\n")
    archivo.write("Mina de Oro \n")
    for i in range(len(mina)):
        archivo.write(str(mina[i]) + "\n")
    archivo.write("El resultado con fuerza bruta fue: " + str(resFB) + "\n" )
    archivo.write("El resultado con programacion dinamica fue: " + str(resPD) + "\n" )
    archivo.write("El tiempo promedio con fuerza bruta fue: " + str(promedioFB) + "\n" )
    archivo.write("El tiempo promedio con programacion dinamica fue: " + str(promedioPD)+ "\n" )
    archivo.close()

main()
