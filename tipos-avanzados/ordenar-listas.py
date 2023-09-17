numeros = [2, 4, 1, 45, 75, 22]

numeros.sort()  # ordena los elementos de menor a mayor
# ordena los elementos de mayor a menor usando el valor de reverse
# al cual obligatoriamente se le debe de dar el valor booleano de True
# numeros.sort(reverse=True)
print(numeros)
# el metodo sorted al ser utilizado devuelve una nueva lista totalmente diferente a la original
numeros_al_reves = sorted(numeros)  # y los ordena
numeros_al_reves = sorted(numeros, reverse=True)  # se ordenan al reves
numeros_al_reves.remove(75)
print(numeros_al_reves)

usuarios = [[4, "chanchito"],
            [5, "jorge"],
            [7, "matias"]
            ]
usuarios.sort()  # organiza los elementos solo si el indice esta al inicio del elemento

users2 = [["jorge", 5], ["carolina", 8], ["felipe", 9]]


def ordenar(elemento):
    return elemento[1]


users2.sort(key=ordenar, reverse=True)
print(users2)
