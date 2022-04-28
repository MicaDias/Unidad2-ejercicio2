from ViajeroFrecuente import ViajeroFrecuente
from ManejadorViajero import ManejadorViajero
from Menu import Menu
import csv
if __name__ =='__main__':
    manejador=ManejadorViajero()
    manejador.cargarDatos()
    num=int(input("Ingrese el numero de Viajero:"))
    #pruebaa
    pos=manejador.buscarViajero(num)
    if pos!=-1:
        print("Se encontro el numero")
        menu=Menu()
        menu.lanzarMenu(manejador,pos)
    else:
        print("No se encontro")