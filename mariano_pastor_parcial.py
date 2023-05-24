# Pastor Mariano 1H Tutor Alejo
import json
ubicacion = "dt.json"

                     
def abrir_json(ubicacion : str)->dict:
    with open(ubicacion) as archivo:
        estrellas_nba = json.load(archivo)
        jugadores_nba = estrellas_nba["jugadores"]
        return jugadores_nba


#Mostrar la lista de todos los jugadores del Dream Team. 
#Con el formato:
#Nombre Jugador - Posición. Ejemplo:

def mostrar_datos(lista : list, v_1 : str, v_2 : str)->list:
    pass
   

all_stars = abrir_json(ubicacion)
mostrar_datos(all_stars,"nombre","posicion")
# while True:
#     pregunta = input("ingrese el numero deseado:",
#                      "01) Mostrar la lista de todos los jugadores del Dream Team.,
#                      "02)",
#                      "03)",
#                      "04)",
#                      "05)",
#                      "06)",
#                      "07)",
#                      "08)",
#                      "09)",
#                      "10)",
#                      "11)",
#                      "12)",
#                      "13)",
#                      "14)",
#                      "15)",
#                      "16)",
#                      "17)",
#                      "18)",
#                      "19)",
#                      "20)",)

