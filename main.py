from funciones import *
import time

# Recolección de datos
# ----------------------------------------------------

# Lectura

datos_readable = open("base_de_datos.txt", "r")

datos = datos_readable.read().split("\n")

for x in range(len(datos)):
    datos[x] = datos[x].split(",")
    pass

datos_readable.close()

# Solicitud del input
# ----------------------------------------------------

print("\nVENTA AUTOS <---> COL CENTER 🥬🎧 \n")
print("1 Registrar auto")
print("2 Autos disponibles")
print("3 Compra auto\n")

opcion = input("opcion: ")

while not (opcion.lower() in ["1", "2", "3"]):
    # easter egg
    if opcion in ["baby", "easter egg", "4", "2022", "chicustec", "baki", "negrazo"]:
        print("\n" + "me gusta probar tu boca")
        time.sleep(2)
        print("me vuelvo loco cuando diceeee...")
        time.sleep(3)
        print("que soy el que la provoca!")
        time.sleep(2)
        print("BABY YO QUIERO VERTE DESNUDAAAAA")
        time.sleep(1.5)

    # favor de ingresar una opcion
    print("\nPor favor ingrese el indice de la operacion\n")
    opcion = input("opcion: ")
    pass

# Opciones
# ----------------------------------------------------

if opcion == "1":

    # REGISTRO DE AUTO
    # ------------------------------------------------
    print(title("REGISTRAR"))

    new_data = recolectar_datos()
    new_data.append("DISPONIBLE")
    datos.append(new_data)
    print("AUTO REGISTRADO")

elif opcion == "2":

    # DISPONIBILIDAD DE LOS AUTOS
    # ------------------------------------------------
    print(title("DISPONIBILIDAD"))
    print(tabulacion(avaliable(datos)))


elif opcion == "3":

    # COMPRAR AUTOS
    # ------------------------------------------------
    print(title("COMPRAR"))

    # verifica que el auto esté disponible
    while True:
        list_compra = recolectar_datos()
        if not (list_compra in avaliable(datos)):
            print("\nEste carro no está disponible o ya ha sido vendido, porfavor ingrese otra opción")
            print("\n" + tabulacion(avaliable(datos)))
        else:
            break;
    pass

    # lista de autos a mostrar
    autos_output = []

    # Agrega los datos disponibles al output y cambia el estado de DISPONIBLE a VENDIDO.
    for producto in avaliable(datos):
        if producto == list_compra:
            producto[len(producto) - 1] = "VENDIDO"
            print("\nCarro COMPRADO con EXITO!\n")
        pass
        autos_output.append(producto)
    pass

    # Imprime la tabla mostrando el carro comprado
    print(tabulacion(autos_output))

# Escribir los datos nuevos
# ----------------------------------------------------
datos_editable = open("base_de_datos.txt", "w")
datos_editable.write(encrypt(datos))
datos_editable.close()

print("\nCopyright © - COL CENTER CORP 🥬🎧")