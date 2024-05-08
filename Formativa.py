import os
import time
star="true"
PikachuRoll=4500
OtakuRoll=5000
PulpoVenenoso=5200
AnguilaElectrica=4800
total=0
contador=0

print("Bienvenido a Delivery Sushi ")
os.system="cls"
while star=="true":
    
    Sele=int(input("Seleccione su pedido\n1. Pikachu Roll: $4500\n2. Otaku Roll $5000\n3. Pulpo Venenoso Roll: $5200\n4. Anguila Electrica Roll: $4800 "))
    
    if Sele==1:
        total=total+4500
        r=int(input(f"Has seleccionado un Pikachu Roll por $4500\n ¿Desea agregar otra opcion? (1=Si/2=No) "))
        if r==1:
            continue
        else:
            print(f"Total: $",total)
            contador=1
            break

    if Sele==2:
        total=total+5000
        r=int(input(f"Has seleccionado un Otaku Roll por $5000\n ¿Desea agregar otra opcion? (1=Si/2=No) "))
        if r==1:
            continue
        else:
            print(f"Total: $",total)
            contador=1
            break
    if Sele==3:
        total=total+5200
        r=int(input(f"Has seleccionado un Pulpo Venenoso Roll por $5200\n ¿Desea agregar otra opcion? (1=Si/2=No) "))
        if r==1:
            continue
        else:
            print(f"Total: $",total)
            contador=1
            break
    if Sele==4:
        total=total+4800
        r=int(input(f"Has seleccionado un Anguila Electrica por $4800\n ¿Desea agregar otra opcion? (1=Si/2=No) "))
        if r==1:
            continue
        else:
            print(f"Total: $",total)
            contador=1
            break                                
while contador==1:
    os.system="cls"
    r=int(input("¿Tiene codigo de descuento?))


