def no_space(texto):
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto


def reverse(texto):
    texto_al_reves = ""
    for char in texto:
        texto_al_reves = char+texto_al_reves
        print(texto_al_reves)
    return texto_al_reves


def es_palindromo(texto):
    texto = no_space(texto)
    texto_al_reves = reverse(texto)
    if texto == texto_al_reves:
        print("es palindromo")
    else:
        print("no es palindromo")
    return texto_al_reves.lower() == texto_al_reves.lower()


es_palindromo("somos o no somos")
