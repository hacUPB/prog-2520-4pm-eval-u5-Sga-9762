# Reto Unidad 5
# Desarrollado por Juan Alejandro Solórzano

start_route = "C:\\Users\\B09S202est"
folder_route = "C:\\Users\\B09S202est\\Documents\\Programacion_JAS\\prog-2520-4pm-eval-u5-Sga-9762"

chc = int(input("**MENÚ PRINCIPAL** Para iniciar el programa, seleccione una opción a continuación:" \
"\n1. Visualizar archivos en la carpeta actual\n2. Visualizar archivos en una carpeta específica.\n3. Procesar archivos (.csv o .txt)" \
"\n4 Salir\n SELECCIÓN: "))

files = []

match chc:
    case 1:
        file = open(folder_route)
        print(file.read())
    case 2:
        name = input("Ingrese el nombre del archivo: ")
        rt = input("Ingrese la ubicación del archivo: ")
        rt.replace("\\", "\\\\")
        route = (rt + "\\" + name)
        print(rt)
        with open(route, "a+", encoding="utf-8") as txtfile:
            ctd = 0
            caracter = txtfile.read(1)
            while caracter != "":
                ctd += 1

        
        
    case 3:
        pass
    case 4: 
        pass