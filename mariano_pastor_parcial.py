# Pastor Mariano 1H Tutor Alejo
import re
import json
ubicacion = "dt.json"
diccionario_para_csv = []

#lista menu de opciones
lista_menu = ["\n-----BUENOS DIAS-----\n",
            "1) Mostrar la lista de todos los jugadores del Dream Team.",
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
            "21) SALIR DEL PROGRAMA."
            "23) Bonus Track: Ver de cada jugador cuál es su posición en cada uno de las estadisticas en un .CSV."]
                     
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
    muestra datos basicos de (2 variables)
    toma lista y variables (dos o 3) 
    retorna una lista con str
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

def mostrar_jugadores(lista: list, v_1: str) -> list:
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
    verificacion = r"^\d+$"
    if re.match(verificacion, numero):
        respuesta = int(numero)
    else:
        respuesta = -1
    return respuesta

def pasaje_a_float(numero : str)->float:
    """
    toma un str, verifica que sea float y lo pasa.
    """
    verificacion = r"^\d.\d+$"
    if re.match(verificacion, numero) or numero.isdigit():
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

def lista_may_men_promedio(lista : list, Valor_1 : str, Valor_2 : str, promedio : float, orden : int)->list:
    lista_a_dar = []
    if orden == 1:
        for persona in lista:
            if persona[Valor_1][Valor_2] > promedio:
                lista_a_dar.append(persona)
    elif orden == 2:
        for persona in lista:
            if persona[Valor_1][Valor_2] < promedio:
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

def corte_segun_rango_dado(lista, dato_uno, dato_dos):
    pregunta = input("Ingrese el numero donde se establecera el corte: ")
    eleccion = pasaje_a_float(pregunta)
    if eleccion == -1:
        print("dato erroneo")
    else:    
        lista_eleccion = lista_may_men_promedio(lista,dato_uno,dato_dos,eleccion,1)
        return lista_eleccion

def impresion_por_rango_mayor(lista_eleccion,dato_uno, dato_dos): 
    estrellas = obtener_lista_datos(lista_eleccion,"nombre",dato_uno,dato_dos,False)
    if len(estrellas) < 1:
        print("Lo lamento, nadie cumple el parametro")
    elif len(estrellas) == 1:
        imprimir_listas(estrellas)
        print("Es el unico jugador que esta por encima del rango seleccionado.")
    else:
        imprimir_listas(estrellas)
        print("Son los jugadores que estan por encima del rango seleccionado.")

while True:
    imprimir_listas(lista_menu)
    pregunta = input("ingrese el numero deseado: ")
    pregunta = pasaje_a_entero(pregunta)
    verificador_de_parametro(lista_menu, pregunta, 0)
    match pregunta:
        case 1:
            estrellas = obtener_lista_datos(all_stars,"nombre","posicion","",True)
            imprimir_listas(estrellas)            
        case 2:
            jugadores = mostrar_jugadores(all_stars,"nombre")
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
            jugadores = mostrar_jugadores(all_stars,"nombre")
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
            jugadores = mostrar_jugadores(all_stars,"nombre")
            imprimir_listas(jugadores)
            pregunta = input("Escriba el nombre del Jugador: ")
            if verificar_alfabetico(pregunta) == True:
                lista_jugadores = obtener_lista_segun_nombre(all_stars, "nombre", pregunta)
                jugador_elegido = listador_segun_parametros(lista_jugadores,"logros","Miembro del Salon de la Fama del Baloncesto")
                a_printear = mostrar_jugadores(jugador_elegido,"nombre")
                if len(a_printear) < 1:
                    print("Lo siento, no es miembro del salon de la fama del baloncesto")
                else:
                    imprimir_listas(a_printear)
                    print("Es miembro del salon de la fama del baloncesto!")
            else:
                print("Lo siento, no ha ingresado un nombre correcto.")  
            pass
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
            lista_promedio = lista_may_men_promedio(all_stars,"estadisticas","porcentaje_tiros_libres",promedio,1)
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
            lista = []
            for jugador in all_stars:
                cantidad = len(jugador["logros"])
                jugador["cantidad_de_logros"] = cantidad
                lista.append(jugador)
            lista = ordenamiento_de_listas(all_stars, "cantidad_de_logros", "",1)
            print("El jugador con mayor cantidad de {0} es {1} con un total de {2}!!!".format(re.sub(r"_"," ","cantidad_de_logros"),lista[-1]["nombre"],
                                                                        lista[-1]["cantidad_de_logros"]))
        case 18:
            corte_segun_rango_dado(all_stars, "estadisticas", "porcentaje_tiros_triples")
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
        case 0:
            print("\nDato erroneo, por favor ingresa una opcion valida.")
        case -1:
            print("\nDato erroneo, por favor ingresa una opcion valida.")