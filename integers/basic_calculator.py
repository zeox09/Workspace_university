n1 = int(input("ingresa primer numero"))
# int permite convertir string en integer
n2 = int(input("ingresa segundo numero"))

suma = n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2
division = n1 / n2

mensaje = f"""para los numeros {n1} y {n2} 
el resultado de la suma es {suma}
el resultado de la resta es {resta}
el resultado de la division es {division}
el resultado de la multiplicacion es {multiplicacion}
"""
print(mensaje)
