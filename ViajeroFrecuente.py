import csv
class ViajeroFrecuente:
    __num_viajero=0
    __dni=''
    __nombre=''
    __apellido=''
    __milla_acum=0
    
    def __init__(self,num_viajero=0, dni='',nombre='',apellido='',milla_acum=0):
        self.__num_viajero=num_viajero
        self.__dni=dni
        self.__nombre=nombre
        self.__apellido=apellido
        self.__milla_acum=milla_acum
    def cantidadTotalMillas(self):
        
        return self.__milla_acum
    def acumularMillas(self,can):
        self.__milla_acum+=can
        return self.__milla_acum
    def canjearMillas(self,can):
        if (can<=self.__milla_acum):
            self.__milla_acum-=can
            print(" se canjearon millas")
        else:
            print("No se pueden canjear las millas")
        return self.__milla_acum    
    def mostrarDatos(self):
        print("Numero:{} DNI:{} Nombre:{} Apellido:{} Cantidad de millas:{} ".format(int(self.__num_viajero),self.__dni,self.__nombre,self.__apellido,int(self.__milla_acum)))

    def verificarNum(self,num):
        return self.__num_viajero==num
    def funcionTest(self):
        viajero1=ViajeroFrecuente(445,'23998889','Alejandra','Cortez',800)
        print("Metodo cantidadTotalMillas")
        print (viajero1.cantidadTotalMillas())
        print("Metodo acumularMillas")
        viajero1.acumularMillas(200)
        print(viajero1.cantidadTotalMillas())
        print("Metodo canjearMillas")
        viajero1.canjearMillas(300)
        print(viajero1.cantidadTotalMillas())
        print("Metodo mostrarDatos")
        viajero1.mostrarDatos()
