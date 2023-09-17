# obligatoriamente debemos indicarle el parametro al argumento momento de iniciar la funcion
def get_product(**datos):
    print(datos)
    # de esta forma se accede a los argumentos que se ingresan en la funcion
    print(datos["id"], datos["name"])


get_product(id="id",
            name="iphone",
            desc="esto es un iphone")
