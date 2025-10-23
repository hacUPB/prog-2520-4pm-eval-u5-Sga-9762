lista = ["cancion 1\n", "cancion 2\n", "cancion 3\n", "cancion 4\n", "cancion 5\n"]
ruta = "C:\\Users\\B09S202est\\Downloads"
file_name = "mymusic.txt"
file_info = ruta + "\\"+file_name
modo = "w"
fp = open(file_info, modo, encoding = "utf-8")
fp.writelines(lista)
fp.close()