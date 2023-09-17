
users = [["jorge", 5], ["carolina", 8], ["felipe", 9]]


def ordenar(elemento):
    return elemento[1]


users.sort(key=lambda el: el[1], reverse=True)
print(users)
nombres = list(map(lambda usuario: usuario[0], users))
