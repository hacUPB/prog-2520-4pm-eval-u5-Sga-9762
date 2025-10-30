ruta = "C:\\Users\\B09S202est\\Downloads"
file_name = "aviones2.txt"
modo = "x" # dado que el archivo no existe en la carpeta, el modo "w" lo crea

fp = open(ruta+"\\"+file_name, modo, encoding="utf-8") # '+' concatena o agrega cadenas de caracteres
make = str(input("Ingrese el modelo del avión: "))
reg = str(input("Ingrese el registro del avión: "))
alt = str(input("Ingrese la altitud máxima del avión: "))

fp.write("Modelo: " +make+"\n""Registro: "+reg+"\n"+"Altitud máxima (ft): "+alt+"\n\n")


fp.close()