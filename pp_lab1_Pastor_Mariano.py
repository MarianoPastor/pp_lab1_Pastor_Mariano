# Pastor Mariano 1H Tutor Alejo
import re
import json
ubicacion = "dt.json"
diccionario_para_csv = []
ruta_bonus_track = "BONUS_TRACK.csv"

#lista menu de opciones
lista_menu = ["\n-----BUENOS DIAS-----\n",
            "1) Mostrar la lista de todos los jugadores del Dream Team y su posicion.",
            "2) Elegir un Jugador y ver todas sus estadisticas.",
            "3) Crear .CSV de jugador seleccionado de punto 2).",
            "4) Buscar un jugador por su nombre y mostrar sus logros.",
            "5) Mostrar el promedio de puntos por partido de todo el equipo del Dream Team.",
            "6) Buscar un nombre y mostrar si ese jugador es miembro del Salón de la Fama del Baloncesto.",
            "7) Mostrar el jugador con la mayor cantidad de rebotes totales.",
            "8) Mostrar el jugador con el mayor porcentaje de tiros de campo.",
            "9) Mostrar el jugador con la mayor cantidad de asistencias totales.",
            "10) Ingresar un valor y ver que jugadores han promediado más puntos por partido que ese valor.",
            "11) Ingresar un valor y ver los jugadores que han promediado más rebotes por partido que ese valor.",
            "12) Ingresar un valor y ver los jugadores que han promediado más asistencias por partido que ese valor.",
            "13) Mostrar el jugador con la mayor cantidad de robos totales.",
            "14) Mostrar el jugador con la mayor cantidad de bloqueos totales.",
            "15) Ingresar un valor y ver los jugadores que hayan tenido un porcentaje de tiros libres superior a ese valor.",
            "16) Mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido.",
            "17) Mostrar el jugador con la mayor cantidad de logros obtenidos",
            "18) Ingresar un valor y ver los jugadores que hayan tenido un porcentaje de tiros triples superior a ese valor.",
            "19) Mostrar el jugador con la mayor cantidad de temporadas jugadas",
            "20) Ingresar un valor y ver los jugadores, ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a ese valor.",
            "22) Ver la cantidad de jugadores en cada posicion.",
            "23) Bonus Track: Ver de cada jugador cuál es su posición en cada uno de las estadisticas en un .CSV.",
            "24) Ver qué jugador tiene las mejores estadísticas en cada valor.",
            "25) Ver la lista de jugadores ordenadas por la cantidad de All-Star de forma descendente.",
            "21) SALIR DEL PROGRAMA."]            
                     
def abrir_json(ubicacion : str)->dict:
    """
    importa de ubicacion un archivo json y lo retorna para trabajar
    """
    with open(ubicacion) as archivo:
        estrellas_nba = json.load(archivo)
        jugadores_nba = estrellas_nba["jugadores"]
        return jugadores_nba
stars = abrir_json(ubicacion)#creamos un volatil para usar
all_stars = stars[:]

def crear_csv(ruta : str, diccionario : dict, tipo_apertura : str):#crea csv
    """
    toma una ruta de acceso str, un diccionario y un str(para modo de apertura)
    crea un csv a partir del mismo
    """
    with open(ruta,tipo_apertura) as archivo:
        lista_fila_1 = []
        lista_fila_2 = []
        for clave, valor in diccionario.items():
            lista_fila_1.append("{0},".format(clave))
            lista_fila_2.append("{0},".format(valor))
        lista_fila_1[-1] = lista_fila_1[-1][0:-1]
        lista_fila_2[-1] = lista_fila_2[-1][0:-1]
        lista_fila_1[-1] += "\n"
        lista_fila_2[-1] += "\n"
        archivo.writelines(lista_fila_1)
        archivo.writelines(lista_fila_2)

def obtener_lista_datos(lista : list, v_1 : str, v_2 : str,v_3 : str ,orden : bool)->list:
    """
    muestra datos basicos de (2 variables)
    toma lista y variables (dos o 3) 
    retorna una lista con str
    """
    lista_a_usar = []
    if orden == True:
        for personas in lista:
            lista_a_usar.append("{0} - {1}".format(personas[v_1],
                                            personas[v_2]))
    elif orden == False:
        for personas in lista:
            lista_a_usar.append("{0} - {1}".format(personas[v_1],
                                            personas[v_2][v_3]))
    return lista_a_usar

def obtener_lista_datos_3_elementos(lista : list, v_1 : str, v_2 : str,v_3 : str , v_4)->list:
    """
    muestra datos basicos de (3 variables)
    toma lista y variables (4) 
    retorna una lista
    """
    lista_a_usar = []
    for personas in lista:
            lista_a_usar.append("{0} - {1} - {2}".format(personas[v_1],personas[v_2],
                                                   personas[v_3][v_4]))
    return lista_a_usar


def obtener_lista_segun_nombre(lista : list, rango : str, busqueda : str)->list:
    """
    crea una lista de todos los mach de busqueda que se le coloquen
    """
    lista_rango = []
    verificacion = r"{0}+".format(busqueda.capitalize())
    for indice in lista: 
        if re.search(verificacion, indice[rango]):
            lista_rango.append(indice) 
    return lista_rango

def imprimir_listas(lista : list):#imprime listas
    """
    imprime lista
    """
    for i in range(len(lista)):
        print(lista[i])

def listar_jugadores(lista: list, v_1: str) -> list:
    """
    crea una lista numerada de lo que queremos mostrar
    toma lista y string
    retorna lista
    """
    lista_a_usar = []
    for indice in range(len(lista)):
        numero = indice + 1
        lista_a_usar.append("{0} - {1}".format(numero, lista[indice][v_1]))
    return lista_a_usar

def formateo_a_lista(diccionario : dict)->list:
    """
    toma un diccionario y crea una lista de str
    """
    lista = []
    for clave, valor in diccionario.items():
        lista.append("{0} : {1}".format(clave,valor))
    return lista 

def pasaje_a_entero(numero: str) -> int:
    """
    Toma un str, verifica que sea entero y lo pasa.
    """
    if re.match(r"^\d+$", numero):
        respuesta = int(numero)
    else:
        respuesta = -1
    return respuesta

def pasaje_a_float(numero : str)->float:
    """
    toma un str, verifica que sea float o entero y lo pasa a float.
    """
    if re.match(r"^\d+\.{1}\d+", numero) or numero.isdigit():
        respuesta = float(numero)
    else:
        respuesta = -1
    return respuesta

def verificador_de_parametro(lista : list, numero : int, agregado : int)->int:
    """
    verifica que un numero este dentro de el len de la lista y permite sumar a ese numero
    toma lista numero y numero a agregar
    retorna numero con o sin correccion
    """
    if numero > len(lista) or numero < 0:
        respuesta = -1
    else:
        respuesta = numero + agregado
    return respuesta

def verificar_alfabetico(dato : str)->bool:
    """
    verifica que el dato este dedntro de los parametros
    a a z minuscula o mayuscula e incluye el espacio
    """
    verificacion = r"^[A-Za-z ]*$"
    devolver = False
    if re.match(verificacion,dato):
        devolver = True
    return devolver

def calcular_promedio(lista : list, acceso_1 : str,acceso_2 : str)->float:
    """
    saca el promedio de una lista
    """
    suma = 0
    divisor = len(lista)
    for star in lista:
        suma = suma + star[acceso_1][acceso_2]
    promedio_final = suma / divisor
    return promedio_final

def ordenamiento_de_listas(lista_original:list, v_1 : str, v_2 : str, orden : int)->list:
    """
    realiza un ordenamiento de lista segun dato solicitado
    """
    lista = lista_original[:]
    rango_a = len(lista)
    flag_swap = True
    while(flag_swap):
        flag_swap = False
        rango_a = rango_a - 1
        if orden == 1:    
            for indice_A in range(rango_a):
                if  lista[indice_A][v_1] > lista[indice_A+1][v_1]:
                    lista[indice_A],lista[indice_A+1] = lista[indice_A+1],lista[indice_A]
                    flag_swap = True
        elif orden == 2:
            for indice_A in range(rango_a):
                if  lista[indice_A][v_1][v_2] > lista[indice_A+1][v_1][v_2]:
                    lista[indice_A],lista[indice_A+1] = lista[indice_A+1],lista[indice_A]
                    flag_swap = True
    return lista

def listador_segun_parametros(lista : list,v_1 : str,v_2 : str)->list:
    """
    genera una lista verificando si se encuentran los datos
    recibe lista y dos datos str
    retorna lista
    """
    lista_a_dar =[]
    for personas in lista:
        if v_2 in personas[v_1]:
            lista_a_dar.append(personas)
    return lista_a_dar

def lista_may_men_promedio(lista : list, Valor_1 : str, Valor_2 : str, promedio : float)->list:
    """
    crea una lista a partir de un corte (promedio)
    """
    lista_a_dar = []
    for persona in lista:
        if persona[Valor_1][Valor_2] > promedio:
            lista_a_dar.append(persona)
    return lista_a_dar

def impresor_mayor_cantidad_segun_dato(lista : list, dato : str):#imprime
    """
    permite ingresarle dato y lista e imprime el  
    el mayor jugador del dato de estadistica seleccionado en esa lista 
    """
    lista = ordenamiento_de_listas(all_stars, "estadisticas", dato,2)
    print("El jugador con mayor cantidad de {0} es {1} con un total de {2}!!!".format(re.sub(r"_"," ",dato),lista[-1]["nombre"],
                                                                        lista[-1]["estadisticas"][dato]))

def corte_segun_rango_dado(lista : list, dato_uno : str , dato_dos : str ):
    """
    realiza una lista cortando los datos segun dato dado
    """
    pregunta = input("Ingrese el numero donde se establecera el corte: ")
    eleccion = pasaje_a_float(pregunta)
    if eleccion == -1:
        print("dato erroneo")
    else:    
        lista_eleccion = lista_may_men_promedio(lista,dato_uno,dato_dos,eleccion)
        return lista_eleccion

def impresion_por_rango_mayor(lista_eleccion : list,dato_uno : str, dato_dos : str): 
    """
    imprime por rango dado una lista
    """
    estrellas = obtener_lista_datos(lista_eleccion,"nombre",dato_uno,dato_dos,False)
    if len(estrellas) < 1:
        print("Lo lamento, nadie cumple el parametro")
    elif len(estrellas) == 1:
        imprimir_listas(estrellas)
        print("Es el unico jugador que esta por encima del rango seleccionado.")
    else:
        imprimir_listas(estrellas)
        print("Son los jugadores que estan por encima del rango seleccionado.")

def listar_segun_logros(lista : list, dato : str, como_ver : str)->list:
    """
    genera un elemento de diccionario averiguando una longitud
    """
    lista = []
    for jugador in all_stars:
        cantidad = len(jugador[dato])
        jugador[como_ver] = cantidad
        lista.append(jugador)
    return lista
        
def impresion_mayor_jugador_logros(lista : list, como_ver : str):#imprime
    """
    imprime por consola el ultimo dato de la lista (en este caso el mayor)
    """
    lista_impresion = ordenamiento_de_listas(lista, como_ver, "",1)
    print("El jugador con mayor cantidad de {0} es {1} con un total de {2}!!!".format(re.sub(r"_"," ",como_ver),lista_impresion[-1]["nombre"],
                                                                lista_impresion[-1][como_ver]))

def CSV_bonus_track():
    """
    crea un .csv con los jugadores rankeados por sus estadisticas, con puntos segun ubicacion
    en lista
    """
    
    lista_segun_logros = listar_segun_logros(all_stars,"logros","cantidad_de_logros")
    lista_temporadas = ordenamiento_de_listas(all_stars,"estadisticas","temporadas",2)
    lista_temporadas = listar_jugadores(lista_temporadas,"nombre") 
    lista_puntos_totales = ordenamiento_de_listas(all_stars,"estadisticas","puntos_totales",2)
    lista_puntos_totales = listar_jugadores(lista_puntos_totales,"nombre") 
    lista_promedio_puntos_por_partido = ordenamiento_de_listas(all_stars,"estadisticas","promedio_puntos_por_partido",2)
    lista_promedio_puntos_por_partido = listar_jugadores(lista_promedio_puntos_por_partido,"nombre")
    lista_rebotes_totales = ordenamiento_de_listas(all_stars,"estadisticas","rebotes_totales",2)
    lista_rebotes_totales = listar_jugadores(lista_rebotes_totales,"nombre")
    lista_promedio_rebotes_por_partido = ordenamiento_de_listas(all_stars,"estadisticas","promedio_rebotes_por_partido",2)
    lista_promedio_rebotes_por_partido = listar_jugadores(lista_promedio_rebotes_por_partido,"nombre")
    lista_asistencias_totales = ordenamiento_de_listas(all_stars,"estadisticas","asistencias_totales",2)
    lista_asistencias_totales = listar_jugadores(lista_asistencias_totales,"nombre")
    lista_promedio_asistencias_por_partido = ordenamiento_de_listas(all_stars,"estadisticas","promedio_asistencias_por_partido",2)
    lista_promedio_asistencias_por_partido = listar_jugadores(lista_promedio_asistencias_por_partido,"nombre")
    lista_robos_totales = ordenamiento_de_listas(all_stars,"estadisticas","robos_totales",2)
    lista_robos_totales = listar_jugadores(lista_robos_totales,"nombre")
    lista_bloqueos_totales = ordenamiento_de_listas(all_stars,"estadisticas","bloqueos_totales",2)
    lista_bloqueos_totales = listar_jugadores(lista_bloqueos_totales,"nombre")
    lista_porcentaje_tiros_de_campo = ordenamiento_de_listas(all_stars,"estadisticas","porcentaje_tiros_de_campo",2)
    lista_porcentaje_tiros_de_campo = listar_jugadores(lista_porcentaje_tiros_de_campo,"nombre")
    lista_porcentaje_tiros_libres = ordenamiento_de_listas(all_stars,"estadisticas","porcentaje_tiros_libres",2)
    lista_porcentaje_tiros_libres = listar_jugadores(lista_porcentaje_tiros_libres,"nombre")
    lista_porcentaje_tiros_triples = ordenamiento_de_listas(all_stars,"estadisticas","porcentaje_tiros_triples",2)
    lista_porcentaje_tiros_triples = listar_jugadores(lista_porcentaje_tiros_triples,"nombre")
    lista_segun_logros = ordenamiento_de_listas(lista_segun_logros,"cantidad_de_logros","",1)
    lista_segun_logros = listar_jugadores(lista_segun_logros,"nombre")
    lista_Michael_Jordan = ["Michael Jordan"]
    lista_Magic_Johnson = ["Magic Johnson"]
    lista_Larry_Bird = ["Larry Bird"]
    lista_Charles_Barkley = ["Charles Barkley"]
    lista_Scottie_Pippen = ["Scottie Pippen"]
    lista_David_Robinson = ["David Robinson"]
    lista_Patrick_Ewing = ["Patrick Ewing"]
    lista_Karl_Malone = ["Karl Malone"]
    lista_John_Stockton = ["John Stockton"]
    lista_Clyde_Drexler = ["Clyde Drexler"]
    lista_Chris_Mullin = ["Chris Mullin"]
    lista_Christian_Laettner = ["Christian Laettner"]

    listas_jugadores = [lista_Michael_Jordan,lista_Magic_Johnson,lista_Larry_Bird,lista_Charles_Barkley,lista_Scottie_Pippen,lista_David_Robinson,
                        lista_Patrick_Ewing,lista_Karl_Malone,lista_John_Stockton,lista_Clyde_Drexler,lista_Chris_Mullin,lista_Christian_Laettner]
    lista_ordenada_por_ranking = [lista_temporadas,lista_puntos_totales,lista_promedio_puntos_por_partido,lista_rebotes_totales,
                                lista_promedio_rebotes_por_partido,lista_asistencias_totales,lista_promedio_asistencias_por_partido,
                                lista_robos_totales,lista_bloqueos_totales,lista_porcentaje_tiros_de_campo,lista_porcentaje_tiros_libres,
                                lista_porcentaje_tiros_triples,lista_segun_logros]
        
    lista_encabezado_csv = ["nombre,"]
    for clave, valor in all_stars[0]["estadisticas"].items():
        clave += ",{0}".format(clave)
        lista_encabezado_csv.append(clave)
    lista_encabezado_csv += ",cantidad_de_logros\n"

    for indice in range(len(lista_ordenada_por_ranking)):
            lista_ordenada_por_ranking[indice] = lista_ordenada_por_ranking[indice][::-1]

    for jugadores in listas_jugadores:
        for lista in lista_ordenada_por_ranking:
            for i in range(len(lista)):
                if re.search(r"{0}".format(jugadores[0]),lista[i]):
                    i = i + 1 
                    jugadores.append(i)

    with open(ruta_bonus_track,"w") as archivo:
            archivo.writelines(lista_encabezado_csv)
            for indice in range(len(listas_jugadores)):
                archivo.writelines("{0}\n".format(listas_jugadores[indice]))

def listador_parametros(lista: list, valor: str) -> list:
    """
    genera un parametro con el valor dado, contavilizando ocurrencias
    """
    a_dar = {}
    for personas in lista:
        for clave, llave in personas.items():
            if clave == valor:
                if llave in a_dar:
                    a_dar[llave] = a_dar[llave]+1
                else:
                    a_dar[llave] = 1
    return a_dar

def pasaje_logro_a_obtencion_numerica(all_stars: list, dato: str) -> list:
    lista = []
    for jugador in all_stars:
        for logros in jugador[dato]:
                if re.match(r"\d veces All-Star", logros) == True:
                    jugador["all-stars"] = re.sub(r"A-Za-z ","",logros)
                    lista.append(jugador)
        return lista


while True:
    imprimir_listas(lista_menu)
    pregunta = input("ingrese el numero deseado:\n ")
    pregunta = pasaje_a_entero(pregunta)
    match pregunta:
        case 1:
            estrellas = obtener_lista_datos(all_stars,"nombre","posicion","",True)
            imprimir_listas(estrellas)            
        case 2:
            jugadores = listar_jugadores(all_stars,"nombre")
            imprimir_listas(jugadores)
            pregunta = input("Seleccione el numero de Jugador: ")
            numero = pasaje_a_entero(pregunta)
            numero = verificador_de_parametro(jugadores, numero, -1)
            if numero == -1:
                print("el numero ingresado es invalido")
            else:
                estadisticas = formateo_a_lista(all_stars[numero]["estadisticas"])
                imprimir_listas(estadisticas)
                diccionario_para_csv = all_stars[numero]["estadisticas"]
                ruta_csv = "all_stars_{0}.csv".format(all_stars[numero]["nombre"][0:4])
        case 3:
            if len(diccionario_para_csv) > 0:
                crear_csv(ruta_csv, diccionario_para_csv,"w")
            else:
                print("primero debe realizarce el punto 2)")
        case 4:
            jugadores = listar_jugadores(all_stars,"nombre")
            imprimir_listas(jugadores)
            pregunta = input("Escriba el nombre del Jugador: ")
            if verificar_alfabetico(pregunta) == True:
                lista_jugadores = obtener_lista_segun_nombre(all_stars, "nombre", pregunta)
                jugador_elegido = obtener_lista_datos(lista_jugadores,"nombre","logros","",True)
                imprimir_listas(jugador_elegido)
            else:
                print("Lo siento, no ha ingresado un dato correcto de busqueda")  
        case 5:
            lista_ordenada = ordenamiento_de_listas(all_stars, "nombre","",1)
            datos = obtener_lista_datos(lista_ordenada,"nombre","estadisticas","promedio_puntos_por_partido",False)
            promedio_general = calcular_promedio(lista_ordenada, "estadisticas","promedio_puntos_por_partido")
            print("El promedio general del equipo es: {0}".format(promedio_general))
            imprimir_listas(datos)
        case 6:
            jugadores = listar_jugadores(all_stars,"nombre")
            imprimir_listas(jugadores)
            pregunta = input("Escriba el nombre del Jugador: ")
            if verificar_alfabetico(pregunta) == True:
                lista_jugadores = obtener_lista_segun_nombre(all_stars, "nombre", pregunta)
                jugador_elegido = listador_segun_parametros(lista_jugadores,"logros","Miembro del Salon de la Fama del Baloncesto")
                a_printear = listar_jugadores(jugador_elegido,"nombre")
                if len(a_printear) < 1:
                    print("Lo siento, no es miembro del salon de la fama del baloncesto")
                else:
                    imprimir_listas(a_printear)
                    print("Es miembro del salon de la fama del baloncesto!")
            else:
                print("Lo siento, no ha ingresado un nombre correcto.")  
        case 7:
            impresor_mayor_cantidad_segun_dato(all_stars, "rebotes_totales")
        case 8:
            impresor_mayor_cantidad_segun_dato(all_stars, "porcentaje_tiros_de_campo")
        case 9:
            impresor_mayor_cantidad_segun_dato(all_stars, "asistencias_totales")
        case 10:
            lista_cortada = corte_segun_rango_dado(all_stars, "estadisticas", "promedio_puntos_por_partido")
            impresion_por_rango_mayor(lista_cortada,"estadisticas", "promedio_puntos_por_partido")
        case 11:
            lista_cortada = corte_segun_rango_dado(all_stars, "estadisticas", "promedio_rebotes_por_partido")
            impresion_por_rango_mayor(lista_cortada,"estadisticas", "promedio_rebotes_por_partido")
        case 12:
            lista_cortada = corte_segun_rango_dado(all_stars, "estadisticas", "promedio_asistencias_por_partido")  
            impresion_por_rango_mayor(lista_cortada,"estadisticas", "promedio_asistencias_por_partido")    
        case 13:
            impresor_mayor_cantidad_segun_dato(all_stars, "robos_totales")
        case 14:
            impresor_mayor_cantidad_segun_dato(all_stars, "bloqueos_totales")
        case 15:
            pregunta = input("Ingrese el numero donde se establecera el corte: ")
            promedio = pasaje_a_float(pregunta)
            lista_promedio = lista_may_men_promedio(all_stars,"estadisticas","porcentaje_tiros_libres",promedio)
            estrellas = obtener_lista_datos(lista_promedio,"nombre","estadisticas","porcentaje_tiros_libres",False)
            if len(estrellas) > 0:
                imprimir_listas(estrellas)
                print("Son los jugadores que estan por encima del rango seleccionado.")        
            else:
                print("lo lamento, nadie cumple con el requisito.")
        case 16:
            lista = ordenamiento_de_listas(all_stars,"estadisticas","promedio_puntos_por_partido",2)
            sin_menor = lista[1:]
            promedio = calcular_promedio(sin_menor,"estadisticas","promedio_puntos_por_partido")
            print("El promedio de puntos por partido excluyendo al jugador que menos puntos anoto es {0}".format(promedio))
        case 17:
            lista_a_imprimir = listar_segun_logros(all_stars,"logros","datos_segun_logros")
            impresion_mayor_jugador_logros(lista_a_imprimir,"datos_segun_logros")
        case 18:
            lista_cortada = corte_segun_rango_dado(all_stars, "estadisticas", "porcentaje_tiros_triples")
            impresion_por_rango_mayor(lista_cortada,"estadisticas", "porcentaje_tiros_triples")
        case 19:
            impresor_mayor_cantidad_segun_dato(all_stars, "temporadas")
        case 20:
            lista = ordenamiento_de_listas(all_stars,"posicion","",1)
            lista_depurada = corte_segun_rango_dado(lista, "estadisticas", "porcentaje_tiros_de_campo")
            lista_a_imprimir = obtener_lista_datos_3_elementos(lista_depurada, "nombre","posicion","estadisticas","porcentaje_tiros_de_campo")
            imprimir_listas(lista_a_imprimir)
        case 21:
            print("\nGracias por usar el programa!")
            break
        case 23:
            CSV_bonus_track()
        case 22:
            operador = listador_parametros(all_stars,"posicion")
            print(operador)
        case 24:
            for valor, llave in all_stars[0]["estadisticas"].items():
                impresor_mayor_cantidad_segun_dato(all_stars, valor)
        case 25:
            lista = pasaje_logro_a_obtencion_numerica(all_stars,"logros")
            print(lista)
            lista = ordenamiento_de_listas(lista,"all-stars","",1)
            print(lista)
            lista = lista[::-1]
            print(lista)
            print("Nombre: {0} Veces All Star: {0}\n".format(lista["nombre"],lista["all-Stars"]))
            
        case _:
            print("\nDato erroneo, por favor ingresa una opcion valida.")


                
""
"""
2
Mostrar la lista de jugadores ordenadas por la cantidad de All-Star de forma descendente. La salida por pantalla debe tener un formato similar a este:
Michael Jordan (14 veces All Star)
Magic Johnson (12 veces All-Star)
...


4
Determinar qué jugador tiene las mejores estadísticas de todos.

"""