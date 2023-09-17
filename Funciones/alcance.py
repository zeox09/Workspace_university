saludo = "hola global"  # alcance global


def saludar():
    saludo = "hello world"
    print(saludo)
# es obligatorio definir antes de hacer el llamado, por cuestiones de alcance


def saluda_chanchito():
    saludo = "hello world"
    print(saludo)


def saludando():
    saludo = "hello world"
    print(saludo)


saludando()
print(saludo)
saludando()
# utilizar variables globales es una mala practica!
