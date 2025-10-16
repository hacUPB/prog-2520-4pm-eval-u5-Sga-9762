#1. Abrir el archivo
txt = open("C:\\Users\\B09S202est\\Desktop\\texto_random.txt", "r", encoding="utf-8")
#2. Leer el archivo

for i in range(3):
    txt.readline()
txt.readline(5)
datos = txt.readline(7)
#3. Cerrar el archivo
txt.close()
print(datos)
