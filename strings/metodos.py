# en este codigo muestro cada uno de los metodos strings que existen en python
text = "Hello my name is Jorge Villan, I am 23 years old and I am a student of Software Engineering and I am also a technologist in analysis and development of information."
print(text.upper())  # caracteres en mayusculas
print(text.lower())  # caracteres en minusculas
print(text.capitalize())  # primera letra en mayuscula
print(text.title())  # cada primer letra de cada palabra en mayuscula
print(text.strip())  # elimina todos los espacios del texto
print(text.lstrip())  # elimina los espacios de la izquierda
print(text.rstrip())  # elimina los espacios de la derecha
print(text.find("Jorge"))  # busca lo que queremos encontrar dentro del texto
# reemplaza el valor que queremos dentro del texto
print(text.replace("hello", "hola"))
print("Jorge" in text)  # busca el valor que deseemos y devuelve un boolean
# realiza la misma busqueda anterior pero si no lo encuentra devuelve True
print("student" not in text)
