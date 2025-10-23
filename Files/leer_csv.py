'''
import csv
humedad = []
with open('C:\\Users\\B09S202est\\Documents\\Programacion_JAS\\Variables.csv', 'r') as csvfile: 
    lector = csv.reader(csvfile, delimiter=';') # método reader
    encabezado = next(lector)
    for fila in lector:
        dato = fila[2]
        n_dato = float(dato.replace(",", "."))
        humedad.append(n_dato)


print(f"**{encabezado[2]}**")
print(humedad)
'''

# Tarea: crear la lista de temperatura, humedad y presión, y leer los datos del archivo

import csv
temp = []
humedad = []
presion = []
with open('C:\\Users\\B09S202est\\Documents\\Programacion_JAS\\Variables.csv', 'r') as csvfile: 
    lector = csv.reader(csvfile, delimiter=';') # método reader
    encabezado = next(lector)
    for fila in lector:
        tp = int(fila[0])
        temp.append(tp)
        hm = int(fila[1])
        humedad.append(hm)
        ps = fila[2]
        ps = float(ps.replace(",", "."))
        presion.append(ps)


print(f"**{encabezado[0]}**")
print(temp)
print(f"**{encabezado[1]}**")
print(humedad)
print(f"**{encabezado[2]}**")
print(presion)