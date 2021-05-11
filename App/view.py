"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
import tracemalloc
import time

def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def getMemory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def deltaMemory(start_memory, stop_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory



"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
crimefile = 'user_track_hashtag_timestamp-5pct.csv'
contextfile = 'context_content_features-5pct.csv'

def printMenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("i- Inicializar analizador")
    print("c- Cargar información")
    print('1- Requerimiento 1  ♥ ♥ ♥ ♥')
    print('2- Requerimiento 2  ♠ ♠ ♠ ♠')
    print('3- Requerimiento 3  ♣ ♣ ♣ ♣')
    print('4- Requerimiento 4  ♦ ♦ ♦ ♦')
    print('5- Requerimiento 5  ♦ ♣ ♠ ♥')
    print("0- Salir")
    print("*******************************************")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if inputs[0] == 'i':
        print("\nInicializando...Por favor, espere en linea.")
        # cont es el controlador que se usará de acá en adelante
        cont = controller.init()
        print("\nAgradecemos su estadia en la linea.")
        print("\nInicializado correctamente!")

    elif inputs[0] == 'c':
        print("\nCargando información de los eventos...")
        controller.loadData(cont, crimefile,contextfile)
        print('Eventos cargados: ' + str(controller.crimesSize(cont)))
        print('Altura del arbol: ' + str(controller.indexHeight(cont)))
        print('Elementos en el arbol: ' + str(controller.indexSize(cont)))
        print('Menor Llave: ' + str(controller.minKey(cont)))
        print('Mayor Llave: ' + str(controller.maxKey(cont)))

        print('Cantidad de artistas: ' + str(controller.autoresSize(cont)))
    elif int(inputs[0])==1:
        caracteristica = input('Digite la característica de contenido: ').lower()   
        valormin = input('Digite el valor mínimo de la característica: ')
        valormax = input('Digite el valor máximo de la característica: ')
        print("*******************************************")

        delta_time = -1.0
        delta_memory = -1.0
        tracemalloc.start()
        start_time = getTime()
        start_memory = getMemory()

        req1 = controller.req1(cont[caracteristica],valormin,valormax)
        print('El total de los eventos de escucha es',req1[0], 'y el número de artistas únicos (sin repeticiones) es',req1[1])
        print("*******************************************")

        stop_memory = getMemory()
        stop_time = getTime()
        tracemalloc.stop()
        delta_time = stop_time - start_time
        delta_memory = deltaMemory(start_memory, stop_memory)

        print('tiempo' , delta_time , '|| memoria' , delta_memory)

    elif int(inputs[0])==2:
        valorminimoenergy = input('Digite el Valor mínimo de la característica Energy: ')
        valormaximoenergy = input('Digite el Valor máximo de la característica Energy: ')
        valorminimodance = input('Digite el Valor mínimo de la característica Danceability: ')
        valormaximodance = input('Digite el Valor máximo de la característica Danceability: ')

        delta_time = -1.0
        delta_memory = -1.0
        tracemalloc.start()
        start_time = getTime()
        start_memory = getMemory()

        controller.req2y3(cont, valorminimoenergy,valormaximoenergy,valorminimodance,valormaximodance)
        
        stop_memory = getMemory()
        stop_time = getTime()
        tracemalloc.stop()
        delta_time = stop_time - start_time
        delta_memory = deltaMemory(start_memory, stop_memory)

        print('tiempo' , delta_time , '|| memoria' , delta_memory)

    elif int(inputs[0])==3:
        valorminimoenergy = input('Digite el Valor mínimo de la característica Instrumentalness: ')
        valormaximoenergy = input('Digite el Valor máximo de la característica Instrumentalness: ')
        valorminimodance = input('Digite el Valor mínimo de la característica Tempo: ')
        valormaximodance = input('Digite el Valor máximo de la característica Tempo: ')

        delta_time = -1.0
        delta_memory = -1.0
        tracemalloc.start()
        start_time = getTime()
        start_memory = getMemory()

        controller.req2y31(cont, valorminimoenergy,valormaximoenergy,valorminimodance,valormaximodance)

        stop_memory = getMemory()
        stop_time = getTime()
        tracemalloc.stop()
        delta_time = stop_time - start_time
        delta_memory = deltaMemory(start_memory, stop_memory)

        print('tiempo' , delta_time , '|| memoria' , delta_memory)
        
    elif int(inputs[0])==4:
        nuevogenero = input('Desea agregar un nuevo genero? (si o no): ').lower()
        if nuevogenero == 'si':
            nuevonombre = input('Ingrese el nombre: ')
            tempomin = input('Valor mínimo del Tempo: ')
            tempomax = input('Valor máximo del Tempo: ')
            controller.anadirgenero(cont,nuevonombre,tempomin,tempomax)
            print("*******************************************")
            print('Genero añadido exitosamente!!!!!!')
            print("*******************************************")

        print("*******************************************")

        listageneros = input('Ingrese la lista de géneros musicales que se desea buscar: ').strip().split(',')

        delta_time = -1.0
        delta_memory = -1.0
        tracemalloc.start()
        start_time = getTime()
        start_memory = getMemory()

        listageneroscontitlexd = []
        for i in listageneros:
            listageneroscontitlexd.append(i.title())

        

        for genero in listageneroscontitlexd:
            print('☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻')
            print('♥♦♣♠',genero.upper(), '♥♦♣♠')
            
            x = controller.gfdhdfhsagfas(cont,genero)
            totaleventos = controller.contareventos(x)
            print('El total de eventos es: ',totaleventos)
        '''
        lista = controller.gfdhdfhsagfas(cont)
        for listaTAD in lista:
            size = lt.size(listaTAD)
            print('El tamaño de ')'''

        stop_memory = getMemory()
        stop_time = getTime()
        tracemalloc.stop()
        delta_time = stop_time - start_time
        delta_memory = deltaMemory(start_memory, stop_memory)

        print('tiempo' , delta_time , '|| memoria' , delta_memory)


    else:
        sys.exit(0)
sys.exit(0)





































































