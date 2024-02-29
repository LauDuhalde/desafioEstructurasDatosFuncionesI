import sys
archivo = sys.argv[1]

#Lee el archivo y guarda el contenido en la variable texto
with open(archivo, 'r') as file:
    texto = file.read()

#Transforma el texto en una lista de palabras al separar
palabras = texto.split(' ')

#Conjuntos para almacenar elementos únicos
caracteres_diferentes = set()
palabras_unicas = set(palabras) #palabras es una lista por lo que se puede transformar directamente en conjunto

for palabra in palabras_unicas:
    for caracter in palabra:
        caracteres_diferentes.add(caracter)
        
#Ya que hicimos split por espacio, este no se contará, por lo que se debe sumar
print(f"El número de caracteres distintos es: {len(caracteres_diferentes)+1}")
print(f"El número de palabras distintas es: {len(palabras_unicas)}")