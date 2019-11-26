# Code to generate the main menu
from .remote_data import descargaDatos
from .dm import muestraLosDatos, ordenarPor

def creaMenu():
    menu=("1.- Descarga Top Artistas", 
            "2.- Descarga Top Canciones", 
            "3.- Ordenar por nombre",
            "4.- Ordenar por listeners", 
            "5.- Mostrar datos",
            "6.- Salir")
            
    funciones = {menu[0]: descargaDatos, menu[1]:descargaDatos,
                 menu[2]: ordenarPor, menu[3]: ordenarPor,
                 menu[4]:muestraLosDatos, menu[5]:exit
                 }
    
    return (menu, funciones)