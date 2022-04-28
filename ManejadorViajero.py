from ViajeroFrecuente import ViajeroFrecuente
import csv
class ManejadorViajero:
    __lista=[]

    def __init__(self):
        self.__lista=[]
    def agregar(self,viajero):
        if type(viajero)==ViajeroFrecuente:
            self.__lista.append(viajero)
        else:
            print("No se puede agregar.")
    def cargarDatos(self):
        #abrir el archivo y guardar los datos en la lista
        archivo=open('Viajeros.csv')
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        for fila in reader:
            if bandera:
                #saltear cabecera
                bandera= not bandera
            else:
                num_viajero=int(fila[0])
                dni=fila[1]
                nombre=fila[2]
                apellido=fila[3]
                millas_acum=int(fila[4])
                viajero=ViajeroFrecuente(num_viajero,dni,nombre,apellido,millas_acum)
                self.agregar(viajero)
        archivo.close()
    def buscarViajero(self,num):
        i=0
        lon=len(self.__lista)
        bandera=True
        while(i<lon and bandera):
            if self.__lista[i].verificarNum(num):
                bandera=False
            else: 
                i+=1
        resultado=0
        if bandera:
            resultado=-1
        else:
            resultado=i
        return resultado 
    def verificarMillas(self,pos):
        print("La cantidad de millas es:",self.__lista[pos].cantidadTotalMillas())
    def sumarMillas(self,pos,can):
        print("La Cantidad de millas es:", self.__lista[pos].acumularMillas(can))
    def restarMillas(self,pos,can):
        #arreglar
        print("La cantidad de millas restantes es:", self.__lista[pos].canjearMillas(can))
    def testManejador(self):
        manejador1=ManejadorViajero()
        print("Metodo agregar:")
        manejador1.agregar(ViajeroFrecuente(121,'34567890','Mica','Dias',600))
        manejador1.agregar('Rocio')
        print("Metodo cargarDatos:")
        manejador1.cargarDatos()
        print("Metodo buscarviajero:")
        i=manejador1.buscarViajero(123)
        print("MetodoverificarMillas:")
        manejador1.verificarMillas(i)
        print("Metodo sumarMillas")
        manejador1.sumarMillas(i,200)
        print("Metodo restarMillas")
        manejador1.restarMillas(i,300)   