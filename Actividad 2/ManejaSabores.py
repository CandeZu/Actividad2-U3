import csv
from ClaseSabor import Sabor

class ManejaSabores:
    __listaSabores = None

    def __init__(self):
        self.__listaSabores = []

    def testSabores(self):
        archivo = open('sabores.csv')
        reader = csv.reader(archivo,delimiter=',')
        for fila in reader:
            nombre = (fila[0])
            descripcion = fila[1]
            self.agregarSabor(Sabor(nombre,descripcion))
        
    def agregarSabor(self,sabor):
        self.__listaSabores.append(sabor)
    
    def getListaSabores(self):
        return self.__listaSabores
    
    def getSabor(self,identificador):
        identificador-=1
        return self.__listaSabores[identificador]
    