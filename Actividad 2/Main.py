from ClaseHelado import Helado
from ClaseSabor import Sabor
from ManejaHelados import ManejaHelados
from ManejaSabores import ManejaSabores

def imprimir():
    print('')
    print('''---------Menu-----------
    (1) Registrar una venta
    (2) Mostrar el nombre de los 5 sabores de helado más pedidos.
    (3) Ingresar un número de sabor y estimar el total de gramos vendidos. 
    Para un helado se estima la cantidad de gramos de cada sabor dividiendo los gramos del helado en la cantidad de sabores.
    (4) Ingresar por teclado un tipo de helado y mostrar los sabores vendidos en ese tamaño considerando todos los helados vendidos.
    (0) Salir. ''')

def gramos():
    print("\n--------------Gramos-----------------")
    print("1. 100gr")
    print("2. 150gr")
    print("3. 250gr")
    print("4. 500gr")
    print("5. 1000gr")
    print("--------------------------------------\n")

def menu():
    band = True
    while band:
        imprimir()
        opcion = int(input('Ingrese una opcion: '))
        if opcion == 1:
            gramos()
            bandera1=True
            tamanioHelado={1: 100,2:150,3:250,4:500,5:1000}
            print('-----Registrar venta-----')
            while bandera1:
                op = int(input('\nIngrese cantidad opción de tamaño en gramos: '))
                if op==1 or op<=5:
                        bandera1=False
                elif op > 5:
                    print("\nOpcion incorrecta, intente de nuevo.")
            sabores=[]
            op1=1
            n=1
            bandera2=True
            
            while bandera2 and n<=4:
                print("\nElegir sabor numero {}\n".format(n))
                for x in manejadorsabores.getListaSabores():
                    print("{}. {}\n{}\n".format(x.getNumero(),x.getNombre(),x.getDescripcion()))
                print("Ingrese 0 pasa salir.")
                op1=int(input("\nIngrese opcion: "))
                if op1<=len(manejadorsabores.getListaSabores()) and op1>0:
                    sabores.append(manejadorsabores.getSabor(op1))
                    n+=1
                elif op1==0:
                    bandera2=False
                else:
                    print("\nOpcion incorrecta. Intente de nuevo.")
            if len(sabores)>0:
                nuevoHelado=Helado(tamanioHelado[op],sabores)
                manejadorHelado.setHelado(nuevoHelado)
                print("\nVenta realizada.")

        elif opcion == 2:
            mayores=manejadorHelado.getMayor(manejadorHelado,manejadorSabor)
            print("Los sabores más pedidos son:")
            for s in mayores:
                print(s)
        
        elif opcion == 3:
            print(" ")
            for x in manejadorSabor.getSabores():
                print("{}. {}\n{}\n".format(x.getNumero(),x.getNombre(),x.getDescripcion()))
            n=int(input("Numero de sabor para mostrar total de gramos vendidos: "))
            manejadorHelado.getTotalGramo(n)
        
        elif opcion == 4:
            tamanioHelado={1: 100,2:150,3:250,4:500,5:1000}
            gramos()
            op=int(input("Ingrese opcion: "))
            lista=manejadorHelado.getTotalSaboresV(op)
            for j in lista:
                print(j)

        elif opcion == 0:
            print('Adios')
            band=False

        else:
            print('Opción no válida, vuelva a ingresar.')



if __name__ == '__main__':
    manejadorhelados = ManejaHelados()
    manejadorsabores = ManejaSabores()
    manejadorsabores.testSabores()
    menu()