
# Ejercicio 1
'''
fp = open("Files/texto_ej1.txt","r")
datos = fp.read(5)
print(datos)
datos = fp.read(5)
print(datos)
fp.close()

'''
'''
1. ¿Cuál es la diferencia entre la primera y la segunda llamada al método read()?
R/ En la primera llamada, se leen los primeros 5 caracteres, y el puntero queda en la ubicación del caracter 5. Cuando se vuelva a llamar,
se empieza a leer desde la ubicación en la que quedó (en la primera llamada).
2. ¿Por qué no se imprimen los mismos datos, si el código es el mismo en ambas operaciones de lectura?
R/ Porque el puntero lee diferentes datos de acuerdo a su ubicación; tal y como se respondió en la pregunta anterior, el puntero empieza a
leer los caracteres desde ubicaciones diferentes cada vez que se llama a read(), y por ello los datos mostrados son diferentes.
3. ¿Por qué debo escribir fp antes de llamar al método read()?
R/ Porque 'read()' es un método, y para poder utilizarse, requiere que se llame a un objeto, en este caso, dicho objeto es 'fp', y el método
'read()' trabaja con los datos que hayan en este objeto.
'''

# Ejercicio 2
'''
fichero = open("Files/texto_ej1.txt","r")
linea = fichero.readline()
print(linea)
linea = fichero.readline()
print(linea)
linea = fichero.readline()
print(linea)
fichero.close()
'''
'''
1. ¿Por qué es importante utilizar el método close()?
R/ Porque cierra el archivo, y así permite que pueda utilizarse en otro programa u aplicación sin causar algún conflicto o problema.
'''

# Ejercicio 2b) Debes crear un script de Python y probar la función readlines(). Escribe tus observaciones en tus apuntes. 

texto = open("Files/texto_ej1.txt", "r", encoding="utf-8")
# **Un archivo es un elemento iterable en Python, puesto que se puede recorrer sus elementos uno por uno (usando funciones como read())**

for a in texto:
    print(a, end="")

texto.close()