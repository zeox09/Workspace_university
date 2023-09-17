users2 = [["jorge", 5], ["carolina", 8], ["felipe", 9]]

# nombres = []
# for usuario in users2:
#     nombres.append(usuario[0])
# print(nombres)
nombres = [usuario[0] for usuario in users2]
# filtrar
nombres = [usuario for usuario in users2 if usuario[1]]
print(nombres)
