mascotas = ["matias", "milo", "alan", "alex", "wolf", "wolf"]
# cuenta cuantas veces se encuentra el elemento dentro de la lista con la funcion count
print(mascotas.count("wolf"))
# busca si existe el elemento dentro de la lista
if "wolf" in mascotas:
    print(mascotas.index("wolf"))
# funcion index busca el elemento deseado y entrega el indice del mismo
print(mascotas.index("milo"))
