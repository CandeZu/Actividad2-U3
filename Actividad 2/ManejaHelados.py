

class ManejaHelados:
    
    __helados = None

def __init__(self, helados):
    
    self.__helados = []

def setHelados(self, unHelado):
    return self.__helados.append(unHelado)

def getMayor(self,helado,manejadorS):
        cantVentas=[]
        mayores=[]
        idMayor=0
        valorMayor=0
        for c in range(len(manejadorS.getSabores())):
            cantVentas.append(0)
        for f in helado.getHelados():
            for sabor in f.getSabores():
                cantVentas[sabor.getNumero()-1]+=1
        for y in range(5):
            for n in range(len(cantVentas)):
                if cantVentas[n]>valorMayor:
                    valorMayor=cantVentas[n]
                    idMayor=n
            if valorMayor>0:
                cantVentas[idMayor]=0
                mayores.append(manejadorS.getSabor(idMayor+1).getNombre())
                valorMayor=0
        return mayores

def getTotalGramo(self,numero):
    helado=self.getHelados()
    total=0
    for s in helado:
        sabores=s.getSabores()
        band=True
        identificador=0
        while band and identificador<len(sabores):
            if sabores[identificador].getNumero()==numero:
                    total+=s.getGramoSabor()
                    band=False
            else:
                identificador+=1
    print("\nGramos totales vendidos: {}".format(total))
    return total

def getTotalSaboresV(self,gramos):
    helado=self.getHelados()
    sabores=[]
    for g in helado:
        if g.getGramos()==gramos:
            for s in g.getSabores():
                sabores.append(s.getNombre())
    return sabores


