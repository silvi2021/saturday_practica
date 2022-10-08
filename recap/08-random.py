import random
import time


#El modulo random tiene varias funciones para trabajar con numeros aleatorios
#La funcion choise es una las mas usada eligiendo un elemento al alzar desde una lista

fruits = ['manzana', 'pera', 'frutillas', 'piña']

#imprimir una fruta al azar

print('redoble de tambores....')

for i in range(1,4):
    print(",")
    time.sleep(0.5)

print('Tu fruta es:')
print(random.choice(fruits))
