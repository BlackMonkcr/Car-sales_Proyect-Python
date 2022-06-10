# recolección de datos                           (funcion)  //Cesar Perales
# -------------------------------------------------------------------------
# La funcion recolectar_datos() debe retornar una lista de 4 elementos, [marc, fab, col, prec] y verificar que sean numeros, años, etc.

def recolectar_datos():
    # Marca
    Marca = input("Marca: ")
    print()

    # Fabricacion
    while True:
        Fabricacion = input("Fabricacion: ")
        try:
            int(Fabricacion)
            break
        except ValueError:
            print("\nFavor de ingresar un NUMERO\n")
    print()

    # Color
    Color = input("Color: ")
    print()

    # Precio
    while True:
        Precio = input("Precio (S/.): ")
        try:
            int(Precio)
            break
        except ValueError:
            print("\nFavor de ingresar un NUMERO\n")
    print()

    return ([Marca, Fabricacion, Color, Precio, "DISPONIBLE"])


pass


# -------------------------------------------------------------------------


# encrypt()                                       (funcion) //Melisa Rivera
# -------------------------------------------------------------------------

# La funcion encrypt(lista), recibe una lista como parametro y devuelve un string en el formato del archivo txt Filas separadas por ("\n") y los elementos de cada FILA separados por una coma ",")

def encrypt(lista):
    L = ""
    for i in range(len(lista)):
        fila = lista[i]
        output = ""
        for j in range(len(fila)):
            output += ("" if j == 0 else ",") + str(fila[j])
        L += ("\n" if i != 0 else "") + output
    return (L)


pass


# -------------------------------------------------------------------------


# tabulacion(lista)                               (funcion) //Aaron Navarro
# -------------------------------------------------------------------------

# la funcion tabulacion(lista) debe tomar como parametro a "lista" y debe retornar un string que contenga la siguiente forma


def tabulacion(base_datos):
    # Definimos listas para añadir la cantidad de caracteres de
    # todos los elementos y de cada columna

    tab_col = []
    tab_total = []

    # Entramos lista por lista y utilizamos un len para contar caracteres de cada
    # elemento "tab_total"

    for x in range(len(base_datos)):
        for i in range(len(base_datos[x])):
            tab_total.append(len(base_datos[x][i]))

    # Definimos una variable y creamos listas para formar parte de la matriz en
    # "tab_col" la cual tiene que ser la misma cantidad que la cantidad de encabezados

    col = 0

    for cabezal in base_datos[0]:
        tab_col.append([])

    # Con este for añadiremos los elementos a cada lista
    # (La información en este caso tendra que estar ordenada en filas)

    for elemento in tab_total:
        tab_col[col].append(elemento)
        col = col + 1
        if col == len(base_datos[0]):
            col = 0

    # Crearemos una lista con los maximos de cada lista de "tab_col"

    lis_max = []
    esp = 2

    for list in tab_col:
        lis_max.append(max(list) + esp)

    # Ahora automatizamos hacer la cadena de .format

    tabulador = ""
    for fil in range(len(base_datos)):
        for colu in range(len(lis_max)):
            tabulador += ("{:<" + str(lis_max[colu]) + "} ").format(
                base_datos[fil][colu])
        tabulador += ("\n" if fil != 0 else "\n" + ((len(tabulador) - 3) * "-") + "\n")
    pass

    # Por ultimo reemplazamos los datos para que sea tabulado
    return tabulador


pass


# -------------------------------------------------------------------------


# avaliable(lista)                                (funcion) //Cesar Perales
# -------------------------------------------------------------------------
# la funcion acaliable(lista) recibe el parametro lista (que es una matriz) y retorna una lista con los elementos vendidos.

def avaliable(lista):
    out = []

    for x in range(len(lista)):
        if not ("DISPONIBLE" in lista[x]) and not ("VENDIDO" in lista[x]):
            out.append(lista[x])
        elif "DISPONIBLE" in lista[x]:  # si esta disponible agregarlo a la lista
            out.append(lista[x])
    return (out)


pass


# -------------------------------------------------------------------------


# title(string)                                   (funcion) //Aaron Navarro
# -------------------------------------------------------------------------
# devuelve el titulo de forma bonita uwu

def title(titulo):
    out = "\n" + "┌" + (len(" " + titulo + " ") * "-") + "┐" + "\n" + "  " + titulo + "  " + "\n" + "└" + (
                len(" " + titulo + " ") * "-") + "┘" + "\n"
    return (out)


pass

# -------------------------------------------------------------------------