# and or y not

# and devuelve un valor si ambas condiciones son verdaderas
gas1 = False
encendido1 = True
# en caso que eso no se cumpla no devuelve ningun valor
if gas1 and encendido1:
    print("puedes avanzar")

# en el caso de or la expresion se dará si el resultado de alguna de las dos se cumple
gas2 = False
encendido2 = True
if gas2 or encendido2:
    print("puedes avanzar")
# el valor de todos debe ser falso para que el resultado de la expesion sea false

# not
# el operador de not le cambia el valor a la otra expresion atribuyendo el valor opuesto
gas3 = True
encendido3 = True
edad = 17
if gas3 and encendido3 and edad > 17:
    print("puedes avanzar")
