numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# feo
# primero = numeros[0]
# segundo = numeros[1]
# tercero = numeros[2]

# cada uno de los elementos de la lista de numeros se guarda en una variable separada
primero, segundo, tercero, *otros1 = numeros
# a la variable de n1 se le otorga el valor del primer elemento de la lista
# y los otros elementos se guardan en una nueva lista llamada otros
n1, *otros, penu, ultio = numeros

print(primero, segundo, tercero)
print(n1, otros, ultio, penu)
