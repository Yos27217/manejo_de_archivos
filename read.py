# Abrir el archivo en modo de lectura
with open("archivo.txt", "r") as f:
    # Leer el contenido del archivo
    contenido = f.read()
    # Imprimir el contenido
    print(contenido)