"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def init():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    analyzer = model.newAnalyzer()
    return analyzer

# Funciones para la carga de datos

def loadData(analyzer, crimesfile,contextfile):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    crimesfile = cf.data_dir + crimesfile
    input_file = csv.DictReader(open(crimesfile, encoding="utf-8"),
                                delimiter=",")
    for crime in input_file:
        model.addCrime(analyzer, crime)


    contextfile = cf.data_dir + contextfile
    input_file1 = csv.DictReader(open(contextfile, encoding="utf-8"),
                                delimiter=',')
    
    for line in input_file1:
        model.addCosas(analyzer,line)
    return analyzer



# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

def autoresSize(analyzer):
    return model.autoresSize(analyzer)

def crimesSize(analyzer):
    """
    Numero de crimenes leidos
    """
    return model.crimesSize(analyzer)

def indexHeight(analyzer):
    """
    Altura del indice (arbol)
    """
    return model.indexHeight(analyzer)


def indexSize(analyzer):
    """
    Numero de nodos en el arbol
    """
    return model.indexSize(analyzer)


def minKey(analyzer):
    """
    La menor llave del arbol
    """
    return model.minKey(analyzer)


def maxKey(analyzer):
    """
    La mayor llave del arbol
    """
    return model.maxKey(analyzer)


def gfdhdfhsagfas(analyzer,genero):
    x = model.checekeador(analyzer, genero)
    return x

def contareventos(listadelistas):
    return model.contareventos(listadelistas)


def req1(map, keylo, keyhi):
    return model.Req1(map, keylo, keyhi)

def req2y3(analyzer, valorminimoenergy,valormaximoenergy,valorminimodance,valormaximodance):
    model.req2y3(analyzer, valorminimoenergy,valormaximoenergy,valorminimodance,valormaximodance)

def req2y31(analyzer, valorminimoenergy,valormaximoenergy,valorminimodance,valormaximodance):
    model.req2y31(analyzer, valorminimoenergy,valormaximoenergy,valorminimodance,valormaximodance)

def anadirgenero(analyzer,nombre,mini,maxi):
    model.anadirgenero(analyzer,nombre,mini,maxi)