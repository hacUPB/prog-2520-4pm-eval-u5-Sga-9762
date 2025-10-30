'''
lista = ["cancion 1\n", "cancion 2\n", "cancion 3\n", "cancion 4\n", "cancion 5\n"]
ruta = "C:\\Users\\B09S202est\\Downloads"
file_name = "mymusic.txt"
file_info = ruta + "\\"+file_name
modo = "r"
 

with open(file_info, modo, encoding="utf-8") as archivo:
    for dato in archivo:
        print(dato, end="")
'''
# Solicitamos al usuario el nombre del archivo a crear
nombre_archivo = input("Ingrese el nombre del archivo de texto: ")
dflt_rt = "C:\\Users\\B09S202est"
fld_chc = int(input("¿En qué carpeta desea agregar el archivo?\n1. Descargas\n2. Documentos\n SELECCION: "))
folder = None
if fld_chc == 1:
    folder = "Downloads"
elif fld_chc == 2:
    folder == "Documents"
info = dflt_rt+"\\"+folder+"\\"+nombre_archivo+".txt"

with open(info, 'w', encoding="utf-8") as archivo:
    # Solicitamos al usuario los datos a escribir en el archivo
    datos = input("Ingrese los datos que desea escribir en el archivo: ")
    archivo.write(datos)

# Ahora usamos 'with' para crear el contexto donde leer los datos del archivo
chc = int(input("¿Desea visualizar el contenido del archivo\n1. Si\n2. No\n Selección: "))
if chc == 1:
    with open(info, 'r', encoding="utf-8") as archivo:
        contenido = archivo.read()
        print("Contenido del archivo:")
        print(contenido)