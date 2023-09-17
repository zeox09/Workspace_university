mascotas = ["wolf", "dog", "cat", "turtle"]
print(mascotas)
mascotas[0] = "bird"  # asi se modifica el elemento dentro de una lista
# con este codigo se imprime un rango de valores dentro de una lista
# si se modifica el numero 0 y se deja vacio python lo interpretara como 0
print(mascotas[0:3])  # print(mascotas[:3])
# al utilizar los valores negativos el valor que será devuelto es el ultimo elemento de la lista de derecha a izquierda
print(mascotas[-1])
print(mascotas[::2])  # hace un salto cada elemento par

numeros = list(range(21))
print(numeros[::2])  # devuelve numeros pares
print(numeros[1::2])  # devuelve numeros inpares
