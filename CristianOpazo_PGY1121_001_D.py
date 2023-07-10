import os
os.system("cls")

menu = '''
   menu
1.-Comprar Entradas
2.-Mostrar Ubicaciones Disponibles
3.-Ver listado de Asistentes
4.-Mostrar Ganancias
5.Salir

'''


precios = '''
PRECIOS
PLATINUM ------------- $120.000
GOLD------------------ $80.000
SILVER---------------- $50.000

'''

fila1 =[1,2,3,4,5,6,7,8,9,10]
fila2 =[11,12,13,"x","x","x",17,18,19,20]
fila3 =[21,22,23,24,25,26,27,28,29,30]
fila4=[31,32,"x",34,35,36,37,38,39,40]
fila5=[41,42,43,44,"x",46,47,48,49,50]
fila6=[51,52,53,54,55,56,57,58,59,60]
fila7=[61,62,63,64,65,66,67,68,69,70]
fila8=[71,72,73,74,75,76,77,78,79,80]
fila9=[81,82,83,84,85,86,87,88,89,90]
fila10=[91,92,93,94,95,96,97,98,99,100]

matriz = [fila1,
          fila2,
          fila3,
          fila4,
          fila5,
          fila6,
          fila7,
          fila8,
          fila9,
          fila10]
listaRut= []
listaPlatinum = []
listaGold = []
listaSilver = []
suma = 0
contPlatinum = 0
contGold = 0
contSilver = 0


def comprarEntradas():
    
    while True:
            try:
                cant_entradas = int(input("ingrese la cantidad de entradas: "))
                if cant_entradas >= 1 and cant_entradas <=3:
                    break
                else:
                    print("error de rango de entradas VIP")
            except:
                print("ha ocurrido una excepcion")
    #fin cantidad de entradas

    while True:
        try:
            print(matriz)
            print(precios)
            nuevaUbicacion = int(input("seleccione un numero de asiento disponible: "))
            for i in range(len(matriz)):
                if nuevaUbicacion[i] == "x":
                        print("asiento no disponible , seleccione otro: ")
                elif nuevaUbicacion[i]!="x":
                        if nuevaUbicacion[i] >=1 and nuevaUbicacion[i] <=20:
                             print("platinum = $120.000")
                             listaPlatinum.append(nuevaUbicacion)
                             monto = 120.000 * cant_entradas
                             suma += monto
                             contPlatinum +=cant_entradas
                             matriz.pop(nuevaUbicacion, "x")
                             break
                        elif nuevaUbicacion[i] >20 and nuevaUbicacion[i] <= 50:
                             print("GOLD = $80.000")
                             listaGold.append(nuevaUbicacion)
                             monto = 80000 * cant_entradas
                             suma += monto
                             contGold += cant_entradas
                             matriz.pop(nuevaUbicacion, "x")
                             break
                        elif nuevaUbicacion[i] >50 and nuevaUbicacion[i] <=100:
                             print("SILVER = $50.000")
                             listaSilver.append(nuevaUbicacion)
                             monto = 50000 * cant_entradas
                             suma += monto
                             contSilver += cant_entradas
                             matriz.pop(nuevaUbicacion, "x")
                             break
                        nuevoRut = int(input("indique su rut: "))
                        if len(nuevoRut) <= 8:
                            listaRut.append(nuevoRut)
                            break
        except:
            print("ha ocurrido una excepcion")
        print("operacion se ha realizado correctamente")
#fin comprar entradas


def mostrarUbicDisp():
     print("mostrando ubicaciones disponibles")
     print(matriz)


def listarAsistentes():
     print(f"{listaRut.sort}")


def mostrarGanancias():
     print("            RESUMEN DE GANANCIAS               ")
     print("TIPO ENTRADA     | CANTIDAD| TOTAL")
     print("+----------------+---------+-------")
     print(f"PLATINUM         |{contPlatinum}          |{120000*cantEntradas}")
     print(f"GOLD             |{contGold}              |{80000* cantEntradas}")
     print(f"SILVER           |{contSilver}            |{50000* cantEntradas}")
     print(F"TOTAL            |{contSilver + contGold + contSilver}|       ")




while True:
     try:
          opc = int(input(menu))
          if opc == 5:
               print("saliendo del sistema")
               print("CRISTIAN OPAZO, 10/07/2023 ")
          elif opc == 1:
               comprarEntradas()
          elif opc == 2:
               mostrarUbicDisp()
          elif opc == 3:
               listarAsistentes()
          elif opc == 4:
               mostrarGanancias()
          else:
               print("opcion invalida")
     except:
          print("ha ocurrido una excepcion")
