# Busqueda secuencial en lista desordenada
def buscar_sin_orden(lista: list, valor) -> int:
    contador = 0
    index = -1
    while ((contador < len(lista)) and (index == -1)):
        if (lista[contador] == valor):
            index = contador
        else:
            contador = contador + 1
    return index
# lista == array -> True in Python
# Busqueda secuencial en lista ordenada
def buscar(array, valor):
    contador = 0
    index = -1
    while ((contador < len(array)) and (index == -1) and (array[contador] <= valor)):
        if (array[contador] == valor):
            index = contador
        else:
            contador = contador + 1
    return index

# Busqueda binaria
def bus_bin(lista, valor):
    inf = 0
    sup = len(lista) - 1
    index = -1
    while ((index == -1) and (inf <= sup)):
        medio = (inf + sup) // 2
        if (lista[medio] == valor):
            index = medio
        elif (lista[medio] > valor):
            sup = medio - 1
        else:
            inf = medio + 1
    return index


def main():
    lista = [5, 8, 3, 11, 7, 9]
    lista.sort()
    print(buscar(lista, 15))
    print(bus_bin(lista, 15))
    
main()
