# Abrir el archivo en modo de lectura
with open("flor.txt", "r") as f:
    # Leer el contenido del archivo usando readlines()
    lineas = f.readlines()
    # Imprimir un mensaje indicando que la información proviene de un script de Python
    print("Información sobre las flores, generada por un script de Python:")
    print("-" * 80)  # Línea de separación
    # Imprimir cada línea del archivo
    for linea in lineas:
        print(linea.strip())  # strip() elimina los saltos de línea al final de cada línea
    print("-" * 80)  # Línea de separación
    print("Fin de la información.")