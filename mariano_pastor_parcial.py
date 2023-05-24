# Pastor Mariano 1H Tutor Alejo
import re
import json
ubicacion = "dt.json"

lista_menu = ["01) Mostrar la lista de todos los jugadores del Dream Team.",
            "02)",
            "03)",
            "04)",
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
            "20)",]
                     
def abrir_json(ubicacion : str)->dict:
    with open(ubicacion) as archivo:
        estrellas_nba = json.load(archivo)
        jugadores_nba = estrellas_nba["jugadores"]
        return jugadores_nba


def mostrar_datos(lista : list, v_1 : str, v_2 : str)->list:
    lista_a_usar = []
    for personas in lista:
        lista_a_usar.append("{0} - {1}".format(personas[v_1],
                                        personas[v_2]))
    return lista_a_usar

def imprimir_listas(lista : list)->None:
    for i in range(len(lista)):
        print(lista[i])

def pasaje_a_entero(numero: str) -> int:
    """
    Toma un str, verifica que sea numérico y lo pasa a entero.
    """
    verificacion = r"^\d+$"
    if re.match(verificacion, numero):
        respuesta = int(numero)
    else:
        respuesta = -1
    return respuesta

def pasaje_a_float(numero : str)->float:
    """
    toma un str, verifica que sea float y lo pasa a float
    """
    verificacion = r"^\d.\d+$"
    if re.match(verificacion, numero):
        respuesta = float(numero)
    else:
        respuesta = -1
    return respuesta

all_stars = abrir_json(ubicacion)
while True:
    pregunta = input("ingrese el numero deseado: ")
    pregunta = pasaje_a_entero(pregunta)
    match pregunta:
        case 1:
            estrellas = mostrar_datos(all_stars,"nombre","posicion")
            imprimir_listas(estrellas)            
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
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
        case _:
            print("\nGracias por usar el programa!")
            break