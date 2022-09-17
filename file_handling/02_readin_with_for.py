#podemos leer las lineas archivos utilizando la estructura de control for.ejemplo
file = open('file_handling/example.txt')

line_number = 1
for line in file:
    print(line_number,line)
    #line_number = line_number + 1
    line_number += 1

file.close()

