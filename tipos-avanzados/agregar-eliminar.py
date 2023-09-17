mascotas = ["matias",
            "milo",
            "alan",
            "alex",
            "wolf",
            "wolf"
            ]

# inserta el valor dentro de la lista en indice indicado
mascotas.insert(1, "melvin")
mascotas.append("darcy")  # inserta el valor al final de la lista

mascotas.remove("wolf")  # elimina el primer elemento
mascotas.pop()  # elimina el ultimo elemento de la lista
mascotas.pop(4)  # elimina el elemento que ha sido iterado dentro del arreglo
del mascotas[0]  # elimina el elemento dependiendo el indice que sea indicado
mascotas.clear()  # limpia la lista eliminando todos sus elementos
print(mascotas)
