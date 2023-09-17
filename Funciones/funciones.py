def hola(nombre, apellido="feliz"):
    print("hola mundo")
    print(f"Bienvenido {nombre}")
    print(f"su apellido es igual a: {apellido}")


hola("jorge", "villan")  # argumento ingresados
hola("jorge")  # hace uso del argumento por defecto
# argumento nombrado, por obligacion cada uno de los parametros de la funcion deve ser nombrado
hola(apellido="Gonzalez", nombre="albeiro")
