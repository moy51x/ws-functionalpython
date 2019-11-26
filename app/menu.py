# Code to generate the main menu
from .remote_data import descargaDatos

def creaMenu():
    menu=("1.- Descarga Top Artistas", 
            "2.- Descarga Top Canciones", 
            "3.- Ordenar por nombre",
            "4.- Ordenar por ranking", 
            "5.- Mostrar datos")
            
    funciones = {menu[0]: descargaDatos, menu[1]:descargaDatos,
                 menu[2]:descargaDatos, menu[3]:descargaDatos,
                 menu[4]:descargaDatos
                 }
    
    return (menu, funciones)