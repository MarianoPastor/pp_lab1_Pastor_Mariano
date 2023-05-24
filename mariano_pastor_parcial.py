# Pastor Mariano 1H Tutor Alejo
import re
import json
ubicacion = "dt.json"
diccionario_para_csv = []

#lista menu de opciones
lista_menu = ["-----BUENOS DIAS-----",
            "01) Mostrar la lista de todos los jugadores del Dream Team.",
            "02) Elegir un Jugador y ver todas sus estadisticas.",
            "03) Crear .CSV de jugador seleccionado de punto 2)",
            "04) Permitir al usuario buscar un jugador por su nombre y mostrar sus logros.",
            "05)",
            "06)",
            "07)",
            "08)",
            "09)",
            "10)",
            "11)",
            "12)",
            "13)",
            "14)",
            "15)",
            "16)",
            "17)",
            "18)",
            "19)",
            "20)",
            "21) Salir del Programa."]
                     
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

def obtener_lista_datos(lista : list, v_1 : str, v_2 : str)->list:
    """
    muestra datos basicos de (2 variables)
    toma lista y dos variables
    retorna una lista con str
    """
    lista_a_usar = []
    for personas in lista:
        lista_a_usar.append("{0} - {1}".format(personas[v_1],
                                        personas[v_2]))
    return lista_a_usar

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
    if re.match(verificacion, numero):
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
    verificacion = r"^[A-Za-z ]*$"
    devolver = False
    if re.match(verificacion,dato):
        devolver = True
    return devolver

while True:
    imprimir_listas(lista_menu)
    pregunta = input("ingrese el numero deseado: ")
    pregunta = pasaje_a_entero(pregunta)
    verificador_de_parametro(lista_menu, pregunta, 0)
    match pregunta:
        case 1:
            estrellas = obtener_lista_datos(all_stars,"nombre","posicion")
            imprimir_listas(estrellas)            
        case 2:
            jugadores = mostrar_jugadores(all_stars,"nombre")
            imprimir_listas(jugadores)
            pregunta = input("Seleccione el Jugador: ")
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
            pregunta = input("Escriba el nombre del Jugador: ")
            if verificar_alfabetico(pregunta) == True:
                jugadore_elegido = obtener_lista_datos(,"nombre","logros")
                imprimir_listas(jugadore_elegido)  
            pass
        case 5:
            pass
        case 6:
            pass
        case 7:
            pass
        case 8:
            pass
        case 9:
            pass
        case 10:
            pass
        case 11:
            pass
        case 12:
            pass
        case 13:
            pass
        case 14:
            pass
        case 15:
            pass
        case 16:
            pass
        case 17:
            pass
        case 18:
            pass
        case 19:
            pass
        case 20:
            pass
        case 21:
            print("\nGracias por usar el programa!")
            break
        case 0:
            print("\nDato erroneo, por favor ingresa una opcion valida.")
        case -1:
            print("\nDato erroneo, por favor ingresa una opcion valida.")