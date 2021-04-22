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


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
crimefile = 'user_track_hashtag_timestamp-small.csv'

def printMenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Inicializar analizador")
    print("2- Cargar información")
    print('3- Requerimiento 1  ♥ ♥ ♥ ♥')
    print('4- Requerimiento 2  ♠ ♠ ♠ ♠')
    print('5- Requerimiento 3  ♣ ♣ ♣ ♣')
    print('6- Requerimiento 4  ♦ ♦ ♦ ♦')
    print('7- Requerimiento 5  ♦ ♣ ♠ ♥')
    print("0- Salir")
    print("*******************************************")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("\nInicializando...Por favor, espere en linea.")
        # cont es el controlador que se usará de acá en adelante
        cont = controller.init()
        print("\nAgradecemos su estadia en la linea.")
        print("\nInicializado correctamente!")

    elif int(inputs[0]) == 2:
        print("\nCargando información de los eventos...")
        controller.loadData(cont, crimefile)
        print('Eventos cargados: ' + str(controller.crimesSize(cont)))
        print('Altura del arbol: ' + str(controller.indexHeight(cont)))
        print('Elementos en el arbol: ' + str(controller.indexSize(cont)))
        print('Menor Llave: ' + str(controller.minKey(cont)))
        print('Mayor Llave: ' + str(controller.maxKey(cont)))
    else:
        sys.exit(0)
sys.exit(0)
