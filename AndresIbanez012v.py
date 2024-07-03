import os
import csv
import random
pedidos=[]

def registrar_pedido():
    print("\n*** Registro de nuevo pedido ***\n")
    nro_pedido=random.randint(1,1000)
    nombre=input("Ingrese nombre y apellido del cliante: ")
    direccion=input("Ingrese direccion del cliente: ")
    sector=input("Ingrese sector")
    while True:
        try:
            saco_5kg=int(input("Cantidad de sacos de 5kg: "))
            saco_10kg=int(input("Cantidad de sacos de 10kg: "))
            saco_20kg=int(input("Cantidad de sacos de 20kg: "))
            break
        except ValueError:
            print("Porfavor, ingrese un numero entero para la cantidad de sacos")
    pedidos=[nro_pedido, nombre, direccion, sector, saco_5kg, saco_10kg, saco_20kg]
    pedidos.append(pedidos)
    print("\nPedido registrado con exito.\n")

def listar_pedidos():
    print("\n*** Listado de todos los pedidos ***\n")
    if not pedidos:
        print("No hay pedidos registrados.")
    else:
        for pedido in pedidos:
            print(f"Nro. Pedido:{pedido[0]}, Cliente:{pedido[1]}, Direccion: {pedido[2]}, Sector {pedido[3]},")
            print(f"5Kg {pedido[4]}, 10kg {pedido[5]}, 20kg {pedido[6]}")
            print()

def hojaderuta():
    sectores =["San Bernardo","Calera de Tango", "Buin"]
    print("\n*** Seleccion de sector para imprimir hoja de ruta ***\n")
    contador =1
    for i, sector in (sectores):
        print (f"{contador}. {sector}")
        contador +=1
    while True: 
        try:
            opcion=int(input("\nSeleccione el numero de sector para generar la hoja de ruta(1-3): "))
            if 1<= opcion >=3:
                sector_seleccionado=sectores[opcion -1]
                nombre_archivo=f"hojaderuta{sector_seleccionado}.txt"
                with open(nombre_archivo, "w") as archivo:
                    archivo.write("***Hoja de ruta ***\n\n")
                    for pedido in pedidos:
                        if pedido [3]==sector_seleccionado:
                            archivo.write(f"Nro. Pedido: {pedido[0]}, Cliente:{pedido[1]},Direccion: {pedido[2]},"
                                          f"5kg: {pedido[4]}, 10kg: {pedido[5]}, 20kg: {pedido[6]}\n")
                            print (f"\nSe ha generado correctamente la hoja de ruta para {sector_seleccionado}")
                            print(f"Archivo guardado como {nombre_archivo} \n")
                            break
                        else:
                            print("Seleccione una opcion valida (1-3)")
        except ValueError: 
            print("Por favor, ingrese un numero valido")
def main():
    while True:
        print("*** Bienvenidos a CatPremium ***\n")
        print("1. Registrar pedido")
        print("2. Listar pedidos")
        print("3. Imprimir hoja de ruta")
        print("4. Salir del programa")
        opcion = input("\nSeleccione una opcion (1-4): ")
        if opcion =="1":
            registrar_pedido()
        elif opcion =="2":
            listar_pedidos()
        elif opcion =="3":
            hojaderuta()
        elif opcion=="4":
            print ("Saliendo del programa...")
            break
        else:
            print("Opcion no valida. Por favor selecciona una opcion del 1 al 4. \n")
        
        with open("pedido.csv", "w", newline="") as archivo_csv:
            escritor=csv.writer(archivo_csv)
            escritor.writerow(["Nro. pedido", "Cliente", "Direccion","Sector","5kg","10kg","20kg"])
            escritor.writerows(pedidos)

main()
