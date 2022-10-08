#la funcion principal para manejar archivos es open()
# esta funcion recibe dos parametros,el nombre del archivo y el modo
#los modos:

#r:para leer y dar error si el archivo no existe
#a: para realizar append (agregar al final).si el archivo no existe lo crea
#w: para escribir elimina el contenido anterior si existe

file = open("file_handling/example.txt","r")
print(file.read)

#a la funcionm read podemos pasar un numero y va a imprimir esa cantidad de caracteres
print(file.read(54))

#tambien existe la funcion readline(),que lee linea por linea
print("ejemplo de readline()")
print(file.readline())
print(file.readline())

#debemos cerrar el archivo luego de usarlo
file.close()

