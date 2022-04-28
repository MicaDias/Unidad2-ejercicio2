from ViajeroFrecuente import ViajeroFrecuente
from ManejadorViajero import ManejadorViajero
class Menu:
    __opciones={}
    def __init__(self):
        self.__opciones={
            '1':self.opcion1,
            '2':self.opcion2,
            '3':self.opcion3,
            '4':self.opcion4,
            '5':self.salir
            }
    def lanzarMenu(self,manejador,pos):
        #Menu opciones
        if type(manejador)==ManejadorViajero:
            i=str(len(self.__opciones))
            opcion=0
            while(i!=opcion):
                print('Menu:')
                print('-Ingrese 1 para consultar cantidad de millas.')
                print('-Ingrese 2 para acumular millas.')
                print('-Ingrese 3 para canjear millas.')
                print('-Ingrese 4 para la funcion test.')
                print('-Ingrese 5 para salir.')
                opcion=input('Ingrese opcion:\n')
                ejecutar=self.__opciones.get(opcion,self.error)
                if (opcion=='1'or opcion=='2' or opcion=='3'):
                    ejecutar(manejador,pos)
                else:
                    ejecutar()
    def opcion1(self,manejador,pos):
        #mostrar la cantidad de millas
        manejador.verificarMillas(pos) 
    def opcion2(self,manejador,pos):
        cant=int(input("Ingresar cantidad de millas para acumular:"))
        manejador.sumarMillas(pos,cant)
    def opcion3(self,manejador,pos):
        canje=int(input("Ingrese la cantidad de millas para canjear:"))
        manejador.restarMillas(pos,canje)
    def opcion4(self):
        manejador2=ManejadorViajero()
        manejador2.testManejador()
        viajero2=ViajeroFrecuente()
        viajero2.funcionTest()
    def error(self):
        #Mensaje cuando ingresa opcion incorrecta
        print('Opción incorrecta')
    def salir(self):
        #Mensaje cuando decide salir
        print('Se cerro el menú')