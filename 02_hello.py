# Las variables son nombres que apuntan a algún valor
# y el valor es de cierto tipo

name = "stranger"

# No pueden comenzar con números ni palabras reservadas
# Es muy aconsejable no utilizar mayúsculas ni acentos.
# Para  separar nombres largos,utilizar el "_"

long_name_variable = "something"
longaniza = " Chillan"

print(name,long_name_variable,longaniza)


# Podemos saber el tipo (class) de variable con la función Type
print(type(longaniza),type(name),type(long_name_variable))

# Otros tipos frecuentes

# int
number = 42
print(type(number))

# bool
is_real = True
not_real = False
print(type(is_real),type(not_real))

#float
decimal = 1.0
print(type(decimal))