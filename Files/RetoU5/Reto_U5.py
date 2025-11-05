# Reto Unidad 5
# Desarrollado por Juan Alejandro Solórzano
'''Declaración de uso de IA: se utilizaron herramientas de inteligencia artificial para permitirle al autor del código
tener una mejor comprensión sobre la lógica de programación para ciertas partes del código, y así desarrollar un programa
que cumpla con las especificaciones requeridas. Ejemplo de uso: búsqueda de métodos o funciones que permitan desarrollar
ciertas tareas en el programa.
'''


def columnacheck(h, k):
    try:
        float(k)
        return True, k
    except:
        return False, None


start_route = "C:\\Users\\(usuario)"
folder_route = "C:\\Users\\(ruta al directorio del archivo)"
#script_route = __file__
bar = "--"*25



files = []
msgs = {"menu_texto": "Submenú de archivos de texto (.txt). A partir de las siguientes opciones, escoja la función que desea " \
        "que el programa realice\n1. Contar cantidad de caracteres en un archivo" \
        "\n2. Reemplazar una palabra por otra en un archivo\n3. Histograma de ocurrencia de vocales en un archivo\
            \n4. Salir\n SELECCIÓN: ", "menu_csv": "Submenú de archivos separados por coma (.csv). A partir de las siguientes opciones, escoja la función que desea " \
        "que el programa realice\n1. Mostrar las primeras 15 filas del archivo" \
        "\n2. Calcular estadísticas de una columna del archivo\n3. Grafico de una columna completa del archivo\
            \n4. Salir\n SELECCIÓN: ", "nombre_txt": "Ingrese el nombre del archivo (con la extensión '.txt' al final): ", 
             "ubicacion_txt": "Ingrese la ubicación del archivo (con un único '\\'): ", "ubicacion_csv": 
             "Ingrese la ubicación del archivo (con un único '\\'): ", 
             "nombre_csv": "Ingrese el nombre del archivo (con la extensión '.csv' al final): ",
              "not_found" : "Error - Archivo no encontrado" }

flag = True
while True:
    chc = int(input("**MENÚ PRINCIPAL** Para iniciar el programa, seleccione una opción a continuación:" \
"\n1. Visualizar archivos en la carpeta actual o en una carpeta específica\n2. Procesar archivos de texto (.txt)" \
"\n3. Procesar archivos separados por comas (.csv)\n4. Salir\n SELECCIÓN: "))
    match chc:
        case 1:
            import os
            current_path = os.getcwd()
            #print(f"Carpeta actual: {current_path}")
            opt = int(input(f"¿En qué carpeta desea visualizar los archivos?\n1. Carpeta actual ({current_path})\n2. Carpeta diferente\n SELECCIÓN: "))
            match opt:
                case 1:
                    files = os.listdir(current_path)
                    print(f"{bar}ARCHIVOS ENCONTRADOS{bar}")
                    n = 0
                    for i in files:
                        print(f"{n+1}: {i}")
                        n += 1
                case 2:
                    folder_name = input("Especifique la ruta a la carpeta a continuación ->> ")
                    print(f"{bar}ARCHIVOS ENCONTRADOS{bar}")
                    files = os.listdir(folder_name)
                    j = 0
                    for i in files:
                        print(f"{j+1}: {i}")
                        j += 1
        case 2:
            fname = input(msgs.get("nombre_txt"))
            rt = input(msgs.get("ubicacion_txt"))
            opt = int(input(msgs.get("menu_texto")))
            match opt:
                case 1:
                    rt = rt.replace("\\", "\\\\")
                    route = rt + "\\" + fname
                    #print(route)
                    try:
                        with open(route, "r", encoding="utf-8") as txtfile:
                            ctd = txtfile.read()
                            caracter = len(ctd)
                            print(f"**El número de caracteres en el archivo {fname} es {caracter} caracteres**")
                    except:
                        print(msgs.get("not_found"))
                case 2:
                    #fname = input(msgs.get("nombre_txt"))
                    #rt = input(msgs.get("ubicacion_txt"))
                    rt = rt.replace("\\", "\\\\")
                    archivo = rt + "\\" + fname
                    wd = input("¿Qué palabra desea reemplazar en el archivo? ->> ")
                    reem = input("¿Por cuál palabra desea sustituirla? ->> ")
                    try:
                        with open(archivo, "r", encoding="utf-8") as file:
                                texto = file.read()
                        try:
                            ntexto = texto.replace(wd, reem)
                            with open(archivo, "w", encoding="utf-8") as file: 
                                file.write(ntexto)
                                print(f"Se ha cambiado la palabra {wd} por {reem} en el archivo {fname}")
                        except:
                            print("Error: no se ha encontrado alguna palabra en el archivo que corresponda a la introducida")
                    except:
                        print(msgs.get("not_found"))
                case 3:
                    #fname = input(msgs.get("nombre_txt"))
                    #rt = input(msgs.get("ubicacion_txt"))
                    rt = rt.replace("\\", "\\\\")
                    route = rt + "\\" + fname
                    valores = []
                    print(f"{bar}**Analizando el archivo**{bar}")
                    with open(route, "r", encoding="utf-8") as txtfile:
                        fl = txtfile.read()
                        a = 0
                        e = 0
                        i = 0
                        o = 0
                        u = 0
                        for j in range(len(fl)):
                            if fl[j] == 'a':
                                a += 1
                            if fl[j] == 'e':
                                e += 1
                            if fl[j] == 'i':
                                i += 1
                            if fl[j] == 'o':
                                o += 1
                            if fl[j] == 'u':
                                u += 1
                        valores.append(a),
                        valores.append(e), 
                        valores.append(i), 
                        valores.append(o), 
                        valores.append(u)
                    categorias = ['A', 'E', 'I', 'O', 'U']
                    import matplotlib
                    import matplotlib.pyplot as plt
                    plt.bar(categorias, valores)
                    plt.title('Histograma')
                    plt.xlabel('Vocales')
                    plt.ylabel('Ocurrencias')
                    print(f"{bar}**Mostrando gráfica comparativa**{bar}")
                    plt.show()
                case 4:
                    print("Saliendo...")
                case _:
                    print("Opción inválida")
                    
        case 3:
            fname = input(msgs.get("nombre_csv"))
            rt = input(msgs.get("ubicacion_csv"))
            rt = rt.replace("\\", "\\\\")
            route = rt + "\\" + fname
            opt = int(input(msgs.get("menu_csv")))
            match opt:
                case 1:
                    import csv
                    try:
                        with open(route, "r", encoding="utf-8") as csvfile:
                            leer = csv.reader(csvfile)
                            j = 1
                            for i in leer:
                                if j <= 15:
                                    print(f"{bar}**Fila {j}{bar}**\n**Contenido:**\n {i}")
                                    j += 1
                    except:
                        print(msgs.get("not_found"))
                case 2:
                    import csv
                    try:
                        with open(route, "r", encoding="utf-8") as csvfile:
                            columna = set() # columna es un set, para evitar duplicados
                            leer = csv.reader(csvfile) #se lee todo el archivo
                            #print(leer)
                            encabezados = next(leer) # dado que el metodo reader() no separa las filas de las columnas, se debe usar el método next() para obtener las columnas de forma individual
                            #print(encabezados)
                            csvfile.seek(0) # se retorna el puntero al inicio del archivo
                            cl = csv.DictReader(csvfile) # se retorna un elemento tipo diccionario legible, cuyo contenido puede leerse al iterar sobre cl
                            for i in cl: # i retorna un diccionario con pares clave-valor, correspondientes al contenido de 'cl'
                                #print(i)
                                for h, k in i.items(): #dado que 'i' es un diccionario, necesito iterar sobre sus claves y valores (h y k, respectivamente)
                                    vestado, valor = columnacheck(h, k) # se llama a la función columnacheck(), que verifica si el valor (k) de la clave (h) es un número
                                    if vestado == True: # si el valor es numérico, entonces se agrega la clave (el nombre de la columna) a un set
                                        nombre = h
                                        columna.add(h)
                                #print(columna)
                                #print(cl)
                            print(f"{bar}COLUMNAS **NUMÉRICAS** ENCONTRADAS EN EL ARCHIVO:{bar}")
                            n = 0
                            nms = {}
                            for i in columna: # i representa el valor de cada elemento de 'columna'
                                print(f"Columna {n+1}: {i}") # columna 1: i
                                nms[n+1] = i # se agrega el nombre de cada columna al diccionario 'nms'
                                n += 1
                            cm = int(input("¿Qué columna desea seleccionar? (su respuesta de forma numérica) ->> "))
                            csvfile.seek(0)
                            lc_columna = csv.DictReader(csvfile)
                            v_max = None
                            v_min = None
                            b = 0
                            col = []
                            sel_colum = nms.get(cm)
                            print(sel_colum)
                            for j in lc_columna: # j devuelve un diccionario con par clave-valor de cada fila (clave: columna)
                                
                                #print(f"{bar}**Columna {cm}**{bar}")
                                #columna.append(j[encabezados[cm-1]])
                                a = j[sel_colum]
                                b = float(a.replace(",", ""))
                                if v_max == None or v_min == None:
                                    v_max = b
                                    v_min = b
                                if b > v_max:
                                    v_max = b
                                if b < v_min:
                                    v_min = b
                                col.append(a)
                            #print(columna)
                            ndatos = len(col)
                            sm = 0
                            for h in col:
                                #print(h)
                                c = h.replace(",","")
                                sm += float(c)
                                #print(sm)
                            prom = sm/ndatos
                            med = col[(ndatos//2)]
                            dv = []
                            for dato in col:
                                m = dato.replace(",","")
                                n = float(m)
                                dv.append(n)
                            import numpy as np
                            desv = np.std(dv)
                            print(f"{bar}**ESTADÍSTICAS DE LA COLUMNA SELECCIONADA**{bar}")
                            print(f"1. Número de datos: {ndatos}\
                            \n2. Valor promedio: {prom}\
                            \n3. Valor máximo: {v_max}\n4. Valor mínimo: {v_min}\
                            \n5. Mediana: {med}\n6. Desviación estándar: {desv}")
                            
                    except FileNotFoundError or OSError:
                        print(msgs.get("not_found"))
                case 3:
                    import csv
                    with open(route, "r", encoding="utf-8") as csvfile:
                        opt = int(input("¿Desea generar un gráfico de dispersión para una de las columnas del archivo?\n1. Si\n2. No\
                                        \nSELECCIÓN:  "))
                        match opt:
                            case 1:
                                columna = set() # columna es un set, para evitar duplicados
                                leer = csv.reader(csvfile) #se lee todo el archivo
                                #print(leer)
                                encabezados = next(leer) # dado que el metodo reader() no separa las filas de las columnas, se debe usar el método next() para obtener las columnas de forma individual
                                #print(encabezados)
                                csvfile.seek(0) # se retorna el puntero al inicio del archivo
                                cl = csv.DictReader(csvfile) # se retorna un elemento tipo diccionario legible, cuyo contenido puede leerse al iterar sobre cl
                                try:
                                    for i in cl: # i retorna un diccionario con pares clave-valor, correspondientes al contenido de 'cl'
                                        #print(i)
                                        for h, k in i.items(): #dado que 'i' es un diccionario, necesito iterar sobre sus claves y valores (h y k, respectivamente)
                                            vestado, valor = columnacheck(h, k) # se llama a la función columnacheck(), que verifica si el valor (k) de la clave (h) es un número
                                            if vestado == True: # si el valor es numérico, entonces se agrega la clave (el nombre de la columna) a un set
                                                nombre = h
                                                columna.add(h)
                                    #print(columna)
                                    #print(cl)
                                    print(f"{bar}COLUMNAS **NUMÉRICAS** ENCONTRADAS EN EL ARCHIVO:{bar}")
                                    n = 0
                                    nms = {}
                                    for i in columna: # i representa el valor de cada elemento de 'columna'
                                        print(f"Columna {n+1}: {i}") # columna 1: i
                                        nms[n+1] = i # se agrega el nombre de cada columna al diccionario 'nms'
                                        n += 1
                                    #print(nms)
                                    cm = int(input("¿Qué columna desea seleccionar? (su respuesta de forma numérica) ->> "))
                                except:
                                    print("No se han encontrado valores en la columna")
                                op_clmn = nms[cm] # nombre de la columna según la opción seleccionada por el usuario
                                print(op_clmn)
                                datos = [] # tabla que contiene los datos de la columna seleccionada
                                csvfile.seek(0)
                                for fila in cl: # bucle 'for' que itera sobre los datos de 'cl'
                                    a = fila[op_clmn] # a la tabla 'datos' se le agrega el valor de cada fila en la columna seleccionada
                                    if a != op_clmn:
                                        datos.append(a)
                                #print(datos)
                                import matplotlib.pyplot as plt
                                x = range(len(datos))
                                #print(x)
                                y = datos
                                plt.scatter(x,y)
                                plt.title("Grafica de dispersión para la columna seleccionada")
                                plt.xlabel("Índice de fila")
                                plt.ylabel(op_clmn)
                                plt.show()
                                chc2 = int(input("¿Desea reorganizar la columna actual?\n1. Si\n2. No\n Selección: "))
                                match chc2:
                                    case 1:
                                        pass
                                    case 2:
                                        opt = int(input("¿Desea reorganizar otra columna?\n1. Si\n2. No\n Selección: "))
                                        match opt:
                                            case 1:
                                                pass
                                            case 2:
                                                pass
                            case 2:
                                pass
                case 4:
                    print("Saliendo...")
        case 4: 
            break
        case _:
            print("Opción inválida")


