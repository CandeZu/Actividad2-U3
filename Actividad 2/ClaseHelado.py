class Helado:
    __gramos=0
    __sabores=[]
    __NumSabor=0

    def __init__(self,gramos,sabores):
        self.__gramos=gramos
        self.__sabores=sabores
        self.__NumSabor=len(sabores)

    def getGramos(self):
        return self.__gramos

    def getSabores(self):
        return self.__sabores

    def getGamoSabor(self):
        return self.__gramos/self.__NumSabor