class Sabor:
    numero = 0
    __numero = 1
    __nombre = ''
    __descripcion = ''
    
    def __init__(self, nombre, descripcion):
        self.setNumero()
        self.__nombre=nombre
        self.__descripcion=descripcion
    
    def getNumero(self):
        return self.__numero
    
    def getNombre(self):
        return self.__nombre
    
    def getDescripcion(self):
        return self.__descripcion
    
    @classmethod
    def getNumeroC(cls):
        cls.numero+=1
        return cls.numero

    def setNumero(self):
        n=self.getNumeroC()
        self.__numero=n