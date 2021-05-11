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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import map as m
from DISClib.DataStructures import listiterator as it
from random import randrange,choice
import datetime
assert config

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newAnalyzer():
    """ Inicializa el analizador

    Crea una lista vacia para guardar todos los crimenes
    Se crean indices (Maps) por los siguientes criterios:
    -Fechas

    Retorna el analizador inicializado.
    """
    analyzer = {'crimes': None,
                'dateIndex': None,
                'autors': None,
                'instrumentalness': None,
                'tempo':None,
                'liveness':None,
                'speechiness':None,
                'danceability':None,
                'valence':None,
                'loudness':None,
                'acousticness':None,
                'energy':None,
                'generos':None
                }

    analyzer['crimes'] = lt.newList('ARRAY_LIST', compareIds)
    analyzer['ids'] = lt.newList('ARRAY_LIST', compareIds)
    analyzer['dateIndex'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareDates)

    analyzer['autors'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareAUTOR)

    analyzer['instrumentalness'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareInt)
    analyzer['tempo'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareInt)
    analyzer['liveness'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareInt)
    analyzer['speechiness'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareInt)
    analyzer['danceability'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareInt)   
    analyzer['valence'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareInt)
    analyzer['loudness'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareInt)
    analyzer['acousticness'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareInt)
    analyzer['energy'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareInt)      

    analyzer['generos']= m.newMap(11,
                                     maptype='CHAINING',
                                   loadfactor=4.0)
                                  
    return analyzer

# Funciones para agregar informacion al catalogo

def newGenre(genero, bpmmin, bpmmax):
    genero = {'genero':None,
        'bpmmin': None,
        'bpmmax': None}
    genero['genero'] = genero
    genero['bpmmin'] = bpmmin
    genero['bpmmax'] = bpmmax
    return genero

def poblargeneros(analyzer):
    Reggae= newGenre('Reggae', 60,90)
    m.put(analyzer['generos'],'Reggae',Reggae)

    Down= newGenre('Down-Tempo', 70,100)
    m.put(analyzer['generos'],'Down-Tempo',Down)

    Chill= newGenre('Chill-Out', 90,120)
    m.put(analyzer['generos'],'Chill-Out',Chill)

    Hip= newGenre('Hip-Hop', 85,115)
    m.put(analyzer['generos'],'Hip-Hop',Hip)

    Jazz= newGenre('Jazz And Funk', 120,125)
    m.put(analyzer['generos'],'Jazz And Funk',Jazz)

    Pop= newGenre('Pop', 100,130)
    m.put(analyzer['generos'],'Pop',Pop)

    RB= newGenre('R&B', 60,80)
    m.put(analyzer['generos'],'R&B',RB)

    Rock= newGenre('Rock', 110,140)
    m.put(analyzer['generos'],'Rock',Rock)

    Metal= newGenre('Metal', 100,160)
    m.put(analyzer['generos'],'Metal',Metal)

def anadirgenero(analyzer,nombre,mini,maxi):
    nuevogenero = newGenre(nombre,mini,maxi)
    m.put(analyzer['generos'],nombre,nuevogenero)


    
    
    

def addCrime(analyzer, crime):
    """
    """
    
    lt.addLast(analyzer['crimes'], crime)
    updateDateIndex(analyzer['dateIndex'], crime)
    return analyzer



def addCosas(analyzer, line):
    lt.addLast(analyzer['ids'], line)
    updateInstrumentalness(analyzer['instrumentalness'], line)
    updateTempo(analyzer['tempo'], line)
    updateLiveness(analyzer['liveness'], line)
    updateSpeechiness(analyzer['speechiness'], line)
    updateDanceability(analyzer['danceability'], line)
    updateValence(analyzer['valence'], line)
    updateLoudness(analyzer['loudness'], line)
    updateAcousticness(analyzer['acousticness'], line)
    updateEnergy(analyzer['energy'], line)
    updateDateIndexAUTOR(analyzer['autors'],line)
    poblargeneros(analyzer)
    return analyzer

def updateInstrumentalness(map, line):
    intrus = line["instrumentalness"]
    entry = om.get(map, intrus)

    if entry is None:
        lista = lt.newList("ARRAY_LIST")
        lt.addLast(lista, line)
        om.put(map, intrus, lista)
        
    else:
        lista = me.getValue(entry)
        lt.addLast(lista, line)
        om.put(map, intrus, lista)

    return map

def updateTempo(map, line):
    intrus = line["tempo"]
    entry = om.get(map, intrus)

    if entry is None:
        lista = lt.newList("ARRAY_LIST")
        lt.addLast(lista, line)
        om.put(map, intrus, lista)
        
    else:
        lista = me.getValue(entry)
        lt.addLast(lista, line)
        om.put(map, intrus, lista)

    return map

def updateLiveness(map, line):
    intrus = line["liveness"]
    entry = om.get(map, intrus)

    if entry is None:
        lista = lt.newList("ARRAY_LIST")
        lt.addLast(lista, line)
        om.put(map, intrus, lista)
        
    else:
        lista = me.getValue(entry)
        lt.addLast(lista, line)
        om.put(map, intrus, lista)

    return map

def updateSpeechiness(map, line):
    intrus = line["speechiness"]
    entry = om.get(map, intrus)

    if entry is None:
        lista = lt.newList("ARRAY_LIST")
        lt.addLast(lista, line)
        om.put(map, intrus, lista)
        
    else:
        lista = me.getValue(entry)
        lt.addLast(lista, line)
        om.put(map, intrus, lista)

    return map

def updateDanceability(map, line):
    intrus = line["danceability"]
    entry = om.get(map, intrus)

    if entry is None:
        lista = lt.newList("ARRAY_LIST")
        lt.addLast(lista, line)
        om.put(map, intrus, lista)
        
    else:
        lista = me.getValue(entry)
        lt.addLast(lista, line)
        om.put(map, intrus, lista)

    return map

def updateValence(map, line):
    intrus = line["valence"]
    entry = om.get(map, intrus)

    if entry is None:
        lista = lt.newList("ARRAY_LIST")
        lt.addLast(lista, line)
        om.put(map, intrus, lista)
        
    else:
        lista = me.getValue(entry)
        lt.addLast(lista, line)
        om.put(map, intrus, lista)

    return map

def updateLoudness(map, line):
    intrus = line["loudness"]
    entry = om.get(map, intrus)

    if entry is None:
        lista = lt.newList("ARRAY_LIST")
        lt.addLast(lista, line)
        om.put(map, intrus, lista)
        
    else:
        lista = me.getValue(entry)
        lt.addLast(lista, line)
        om.put(map, intrus, lista)

    return map

def updateAcousticness(map, line):
    intrus = line["acousticness"]
    entry = om.get(map, intrus)

    if entry is None:
        lista = lt.newList("ARRAY_LIST")
        lt.addLast(lista, line)
        om.put(map, intrus, lista)
        
    else:
        lista = me.getValue(entry)
        lt.addLast(lista, line)
        om.put(map, intrus, lista)

    return map

def updateAcousticness(map, line):
    intrus = line["acousticness"]
    entry = om.get(map, intrus)

    if entry is None:
        lista = lt.newList("ARRAY_LIST")
        lt.addLast(lista, line)
        om.put(map, intrus, lista)
        
    else:
        lista = me.getValue(entry)
        lt.addLast(lista, line)
        om.put(map, intrus, lista)

    return map

def updateEnergy(map, line):
    intrus = line["energy"]
    entry = om.get(map, intrus)

    if entry is None:
        lista = lt.newList("ARRAY_LIST")
        lt.addLast(lista, line)
        om.put(map, intrus, lista)
        
    else:
        lista = me.getValue(entry)
        lt.addLast(lista, line)
        om.put(map, intrus, lista)

    return map

def newDataEntryAUTOR(crime): 
    """
    Crea una entrada en el indice por fechas, es decir en el arbol
    binario.
    """
    entry = { 'lstevents': None}
    
    entry['lstevents'] = lt.newList('ARRAY_LIST')
    return entry

def updateDateIndexAUTOR(map, line):
    """
    Se toma la fecha del crimen y se busca si ya existe en el arbol
    dicha fecha.  Si es asi, se adiciona a su lista de crimenes
    y se actualiza el indice de tipos de crimenes.

    Si no se encuentra creado un nodo para esa fecha en el arbol
    se crea y se actualiza el indice de tipos de crimenes
    """
    artista = line["artist_id"]
    
    entry = om.get(map, artista)

    
    if entry is None:
        datentry = newDataEntryAUTOR(line)
        om.put(map, artista, datentry)
        lt.addLast(datentry['lstevents'],line)
    else:
        datentry = me.getValue(entry)
    
    #addDateIndexAUTOR(datentry, line)
    return map


def updateDateIndex(map, crime):
    """
    Se toma la fecha del crimen y se busca si ya existe en el arbol
    dicha fecha.  Si es asi, se adiciona a su lista de crimenes
    y se actualiza el indice de tipos de crimenes.

    Si no se encuentra creado un nodo para esa fecha en el arbol
    se crea y se actualiza el indice de tipos de crimenes
    """
    occurreddate = crime["created_at"]
    crimedate = datetime.datetime.strptime(occurreddate, '%Y-%m-%d %H:%M:%S')
    entry = om.get(map, crimedate.date())
    if entry is None:
        datentry = newDataEntry(crime)
        om.put(map, crimedate.date(), datentry)
    else:
        datentry = me.getValue(entry)
        
    addDateIndex(datentry, crime)
    return map


def addDateIndex(datentry, crime):
    """
    Actualiza un indice de tipo de crimenes.  Este indice tiene una lista
    de crimenes y una tabla de hash cuya llave es el tipo de crimen y
    el valor es una lista con los crimenes de dicho tipo en la fecha que
    se está consultando (dada por el nodo del arbol)
    """
    lst = datentry['lstcrimes']
    lt.addLast(lst, crime)
    offenseIndex = datentry['offenseIndex']
    offentry = m.get(offenseIndex, crime["track_id"])
    if (offentry is None):
        entry = newOffenseEntry(crime["track_id"], crime)
        lt.addLast(entry['lstoffenses'], crime)
        m.put(offenseIndex, crime["track_id"], entry)
    else:
        entry = me.getValue(offentry)
        lt.addLast(entry['lstoffenses'], crime)
    return datentry


def newDataEntry(crime):
    """
    Crea una entrada en el indice por fechas, es decir en el arbol
    binario.
    """
    entry = {'offenseIndex': None, 'lstcrimes': None}
    entry['offenseIndex'] = m.newMap(numelements=30,
                                     maptype='PROBING',
                                     comparefunction=compareOffenses)
    entry['lstcrimes'] = lt.newList('ARRAY_LIST', compareDates)
    return entry


def newOffenseEntry(offensegrp, crime):
    """
    Crea una entrada en el indice por tipo de crimen, es decir en
    la tabla de hash, que se encuentra en cada nodo del arbol.
    """
    ofentry = {'offense': None, 'lstoffenses': None}
    ofentry['offense'] = offensegrp
    ofentry['lstoffenses'] = lt.newList('ARRAY_LIST', compareOffenses)
    return ofentry


# Funciones para creacion de datos

# Funciones de consulta

def autoresSize(analyzer):
    return om.size(analyzer["autors"])
def crimesSize(analyzer):
    """
    Número de crimenes
    """
    return lt.size(analyzer['crimes'])


def indexHeight(analyzer):
    """
    Altura del arbol
    """
    return om.height(analyzer['dateIndex'])


def indexSize(analyzer):
    """
    Numero de elementos en el indice
    """
    return om.size(analyzer['dateIndex'])


def minKey(analyzer):
    """
    Llave mas pequena
    """
    return om.minKey(analyzer['dateIndex'])


def maxKey(analyzer):
    """
    Llave mas grande
    """
    return om.maxKey(analyzer['dateIndex'])

# Funciones utilizadas para comparar elementos dentro de una lista


def compareIds(id1, id2):
    """
    Compara dos crimenes
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1



def compareDates(date1, date2):
    """
    Compara dos fechas
    """
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1

def compareInt(date1, date2):
    """
    Compara dos fechas
    """
    if (float(date1) == float(date2)):
        return 0
    elif (float(date1) > float(date2)):
        return 1
    else:
        return -1


def compareOffenses(offense1, offense2):
    """
    Compara dos tipos de crimenes
    """
    offense = me.getKey(offense2)
    if (offense1 == offense):
        return 0
    elif (offense1 > offense):
        return 1
    else:
        return -1


def compareAUTOR(offense1, offense2):
    """
    Compara dos tipos de crimenes
    """
    
    if (offense1 == offense2):
        return 0
    elif (offense1 > offense2):
        return 1
    else:
        return -1


# Funciones de ordenamiento


#FUNCIONES XD

def Req1(map, keylo, keyhi):
    valores = om.values(map, keylo, keyhi)
    cantidadEventos = lt.size(valores)

    
    listaartistas = []
    for i in  valores['first']['info']['elements']:
        artista = i['artist_id']
        listaartistas.append(artista)
    '''
    
    listaartistas = lt.newList('ARRAY_LIST')    
    listaartistasunicos = lt.newList('ARRAY_LIST')

    iterador = it.newIterator(valores)
    while it.hasNext(iterador):
        elemento = it.next(iterador)
        artista = elemento['artist_id']
        lt.addLast(listaartistas,artista)


    iterador2 = it.newIterator(listaartistas)
    while it.hasNext(iterador2):
        elemento = it.next(iterador2)    
        check = lt.isPresent(listaartistasunicos, elemento)
        artista = elemento['artist_id']
        if check == 0:
           lt.addLast(listaartistasunicos,artista)
        '''
    
        

    cantidadartistasunicos = len(set(listaartistas))  

    return [cantidadEventos,cantidadartistasunicos]
        


def checekeador(analyzer, i):
    
    genero=m.get(analyzer['generos'], i)
    valorminimo = int(genero['value']['bpmmin'])
    valormaximo = int(genero['value']['bpmmax'])
    
    listadecancionesxd = om.values(analyzer['tempo'], valorminimo, valormaximo)

    listaartistas = []
    for i in  listadecancionesxd['first']['info']['elements']:
        artista = i['artist_id']
        listaartistas.append(artista)
    print('He aqui algunos artistas del genero: ')
    a = 1
    for i in set(listaartistas):
        
        a = a +1
        print(a,i)
        if a ==11:
            break
    print('\n')

        

    cantidadartistasunicos = len(set(listaartistas))
    print('La cantidad de artistas unicos es: ',cantidadartistasunicos)


    return listadecancionesxd
        

def contareventos(listadelistas):
    contador = 0
    iterador2 = it.newIterator(listadelistas)
    while it.hasNext(iterador2):
        elemento = it.next(iterador2)
        iteradorelemento = it.newIterator(elemento)
        while it.hasNext(iteradorelemento):
            diccionarioevento = it.next(iteradorelemento)
            contador = contador + 1

    return contador

def req2y31(analyzer, valorminimoenergy,valormaximoenergy,valorminimodance,valormaximodance):
    listaEnergy = om.values(analyzer['instrumentalness'], valorminimoenergy,valormaximoenergy)
    listaDance = om.values(analyzer['tempo'], valorminimodance,valormaximodance)

    listadefinitiva = lt.newList("ARRAY_LIST")

    idenergy = []
    iddance = []
    
    iteradorenergy = it.newIterator(listaEnergy)
    
    while it.hasNext(iteradorenergy):
        elemento = it.next(iteradorenergy)
        iteradorelemento = it.newIterator(elemento)
        while it.hasNext(iteradorelemento):
            diccionarioevento = it.next(iteradorelemento)
            cancion = diccionarioevento['id']
            
            
            
            idenergy.append(cancion)


    iteradordance = it.newIterator(listaDance)
    while it.hasNext(iteradordance):
        elementodance = it.next(iteradordance)
        iteradordanceelement = it.newIterator(elementodance)
        while it.hasNext(iteradordanceelement):
            diccionarioporeventodance = it.next(iteradordanceelement)
            
            iddance.append(diccionarioporeventodance['id'])
            


    lista_final = []
    for i in idenergy:
        if (i not in lista_final) and (i in iddance):
            lista_final.append(i)
    print(len(lista_final))

    

    veces = 1
    while veces <= 5:
        random = randrange(len(lista_final))
        idaleatorio = lista_final[random]

        iteradorids = it.newIterator(analyzer['ids'])
        while it.hasNext(iteradorids):
            elementoid = it.next(iteradorids)
            if idaleatorio == elementoid['id']:
                print('Track', veces, ':' ,idaleatorio, 'with instrumentalness of', elementoid['instrumentalness'] , ' and tempo of', elementoid['tempo'])
        veces = veces +1


def req2y3(analyzer, valorminimoenergy,valormaximoenergy,valorminimodance,valormaximodance):
    listaEnergy = om.values(analyzer['energy'], valorminimoenergy,valormaximoenergy)
    listaDance = om.values(analyzer['danceability'], valorminimodance,valormaximodance)

    listadefinitiva = lt.newList("ARRAY_LIST")

    idenergy = []
    iddance = []
    
    iteradorenergy = it.newIterator(listaEnergy)
    
    while it.hasNext(iteradorenergy):
        elemento = it.next(iteradorenergy)
        iteradorelemento = it.newIterator(elemento)
        while it.hasNext(iteradorelemento):
            diccionarioevento = it.next(iteradorelemento)
            cancion = diccionarioevento['id']
            
            
            
            idenergy.append(cancion)


    iteradordance = it.newIterator(listaDance)
    while it.hasNext(iteradordance):
        elementodance = it.next(iteradordance)
        iteradordanceelement = it.newIterator(elementodance)
        while it.hasNext(iteradordanceelement):
            diccionarioporeventodance = it.next(iteradordanceelement)
            
            iddance.append(diccionarioporeventodance['id'])
            


    lista_final = []
    for i in idenergy:
        if (i not in lista_final) and (i in iddance):
            lista_final.append(i)
    print(len(lista_final))

    

    veces = 1
    while veces <= 5:
        random = randrange(len(lista_final))
        idaleatorio = lista_final[random]

        iteradorids = it.newIterator(analyzer['ids'])
        while it.hasNext(iteradorids):
            elementoid = it.next(iteradorids)
            if idaleatorio == elementoid['id']:
                print('Track', veces, ':' ,idaleatorio, 'with energy of', elementoid['energy'] , ' and danceability of', elementoid['danceability'])
        veces = veces +1


    
    '''  
    intento 4
    listadefinitiva = lt.newList("ARRAY_LIST")
    x=0
    iteradorenergy = it.newIterator(listaEnergy)
    while it.hasNext(iteradorenergy):
        elemento = it.next(iteradorenergy)
        iteradorelemento = it.newIterator(elemento)
        while it.hasNext(iteradorelemento):
            diccionarioevento = it.next(iteradorelemento)
            iteradordance = it.newIterator(listaDance)
            while it.hasNext(iteradordance):
                print(x)
                x = x +1
                elementodance = it.next(iteradordance)
                print(diccionarioevento['id'])
                posicion = lt.isPresent(elementodance,diccionarioevento)
                if posicion != 00:
                    lt.addLast(listadefinitiva,diccionarioevento)
    print(lt.size(listadefinitiva))
    
    INTENTO 1
    listadefinitiva = lt.newList("ARRAY_LIST")
    x=0 
    iteradorenergy = it.newIterator(listaEnergy)
    while it.hasNext(iteradorenergy):
        elemento = it.next(iteradorenergy)
        iteradorelemento = it.newIterator(elemento)
        while it.hasNext(iteradorelemento):
            diccionarioevento = it.next(iteradorelemento)
            cancion = diccionarioevento['id']
            print(x)
            x = x+1
            print(cancion)
            iteradordance = it.newIterator(listaDance)
            while it.hasNext(iteradordance):
                elementodance = it.next(iteradordance)
                iteradordanceelement = it.newIterator(elementodance)
                while it.hasNext(iteradordanceelement):
                    diccionarioporeventodance = it.next(iteradordanceelement)
                    print(diccionarioporeventodance['id'])
                    if cancion == diccionarioporeventodance['id']:
                        lt.addLast(listadefinitiva, diccionarioporeventodance)

    print(lt.size(listadefinitiva))


    INTENTO 2
    IDsenergy = []

    a = 0
    while a < lt.size(listaEnergy):
        elemento = lt.getElement(listaEnergy,a)

        b = 0
        while b < lt.size(elemento):
            item = lt.getElement(elemento,b)
            IDsenergy.append(item['artist_id'])
            b = b+1
        a = a +1

    IDsdance = []

    



    IDsenergy = []
    IDsdance = []
    for item in listaEnergy['first']['info']['elements']:
        IDsenergy.append(item['energy'])

    for item in listaDance['first']['info']['elements']:
        IDsdance.append(item['danceability'])


    print(IDsenergy)
    print(IDsdance)
    
    
    intento 3


    comparacion=[]
    for item in listaEnergy['first']['info']['elements']:
        if item in listaDance['first']['info']['elements']:
            comparacion.append(item)
    
    if len(comparacion) > 0:
        print ('Ambas listas contienen estos elementos')
        for item in comparacion: print ('%s' % item)
    else:
        print ('No existe ningun elemento igual en las listas')'''


'''
def req5(x):
    delta_time = -1.0
    delta_memory = -1.0
    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    for i in range(1:1000):
        x = x +2
        
    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()
    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)

    print('tiempo' , delta_time , '|| memoria' , delta_memory)

'''