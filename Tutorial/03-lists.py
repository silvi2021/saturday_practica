import math

squares = [1,4,9,16,25]

#desafio: a partir del arreglo anterios crear uno que tenga sus raices
#root = es raiz

roots = []   #aqui estamos diciendo roots va hacer una lista

for number in squares:
    #roots.append(int(number**(1/2))) puede ser asi tambien 1ra opcion
    roots.append(int(math.sqrt(number))) #2da opcion al inicio esta solo root y al final append se van agregando al final


print(roots)


#roots = [1,2,3,4,5]

# sqrt : sqrtS
##square:sq
###root : rt

## append:agrega al final

# reemplar algun elemento del arreglo segun el indice
roots[4] = 6
print(roots)
