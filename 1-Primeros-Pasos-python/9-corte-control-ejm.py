#---------------------------- CORTE DE CONTROL ---------------------------#
#
# Ejemplo de proceso de Corte de control, con dos niveles.
# Acumulado por Codigo de Sucursal, y dentro este, por Codigo de Articulo.
# El resultado se deja en un archivo de texto
#
#------------------------------- FUNCIONES -------------------------------#
def leer(arVentas):
    """
    Funcion que lee una linea del archivo y devuelve los valores leidos
    cod_sucursal, cod_articulo, cant_vendida, imp_total.
    En caso de llegar a fin de archivo devolverá 4 valores vacios
    separados por comas. 
    """
    linea = arVentas.readline()
    if linea:
        devolver = linea.rstrip("\n").split(",")
    else:
        devolver = ("","","","")
    return devolver
def listar_con_corte():
    # Funcion que hace el corte de control por cod_sucursal, y por cod_articulo.
    arVentas = open('ventas.csv','r')
    cod_suc, cod_art, cant, imp = leer(arVentas)
    cant_total_gral = imp_total_gral = 0
    # Corte General Total
    while cod_suc:
        cant_total_suc = imp_total_suc = 0
        cod_suc_anterior = cod_suc
        print("Sucursal: ", cod_suc)
    # Corte por Codigo de Sucursal
    while (cod_suc_anterior == cod_suc):
        cant_total_art = imp_total_art = 0
        cod_art_anterior = cod_art
    # Corte por Codigo de Articulo
    while (cod_suc_anterior == cod_suc and cod_art_anterior == cod_art):
        cant_total_art += int(cant)
        imp_total_art += float(imp)

    cod_suc, cod_art, cant, imp = leer(arVentas)
    print("\t\t", cod_art, "\t{0:6}".format(cant_total_art),
    "\t{0:7.2f}".format(imp_total_art) )
    cant_total_suc += cant_total_art
    imp_total_suc += imp_total_art
    print("Total Sucursal: ", "\t{0:6}".format(cant_total_suc),
    "\t{0:7.2f}\n".format(imp_total_suc) )
    cant_total_gral += cant_total_suc
    imp_total_gral += imp_total_suc
    print("Total General: ", "\t{0:6}".format(cant_total_gral),
    "\t{0:7.2f}\n".format(imp_total_gral) )
    arVentas.close()
    return
#--------------------- Bloque Principal --------------------------#
def main():
    listar_con_corte()
main()
