# Data manipulation functions
import functools

def dameDatosNecesarios(datos, campos_requeridos):
    return [({ cr:x[cr] for cr in campos_requeridos}) for x in datos]


def ordenarPor(datos, dato):
    return list(sorted(datos, key=lambda x: x[dato], reverse=False))


def muestraLosDatos(datos):
    for cadena in dameDatoFormateado(datos):
        print(cadena)


def dameDatoFormateado(datos):
    base_str = "Nombre: {0}, Radioescuchas: {1}, URL: {2}"
    for dato in datos:
        yield base_str.format(dato["name"], dato["listeners"], dato["url"])

