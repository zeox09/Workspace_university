# en este script realizo una calculadora basica de loop infinito
print("Bienvenido a la calculadora")
print("para salir escribe \"salir\"")
print("las operaciones a realizar son Suma,Resta, Multi, Div")
resultado = ""
while True:
    if not resultado:
        resultado = input("ingrese numero: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    operacion = input("ingrese la operacion ")
    if operacion.lower() == "salir":
        break
    n2 = input("Por favor ingresa el numero 2 ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)
    if operacion.lower() == "suma":
        resultado += n2
    elif operacion.lower() == "resta":
        resultado -= n2
    elif operacion.lower() == "multi":
        resultado *= n2
    elif operacion.lower() == "div":
        resultado /= n2
    else:
        print("La operacion ingresada no es valida")

    print(f"el resultado es: {resultado}")
