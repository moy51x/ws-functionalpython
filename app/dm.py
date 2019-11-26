# Data manipulation functions

def dameDatosNecesarios(datos, campos_requeridos):
    list_comp= [({ cr:x[cr] for cr in campos_requeridos}) for x in datos]
    return list_comp


def ordenarPorNombre():
    raise Exception("Not implementation")



def ordenarPorPosicion():
    raise Exception("Not implementation")


def muestraLosDatos(datos):
    for cadena in dameDatoFormateado(datos):
        print(cadena)


def dameDatoFormateado(datos):
    base_str = "Nombre: {0}, Radioescuchas: {1}, URL: {2}"
    for dato in datos:
        yield base_str.format(dato["name"], dato["listeners"], dato["url"])