# Abrir el archivo binario en modo de lectura binaria ('rb') usando la función open()
file = open('azul.bin', 'rb')
# Leer el contenido del archivo usando el método.read() y almacenarlo en la variable binary_data
binary_data = file.read()
# Cerrar el archivo usando el método.close()
file.close()
# Imprimir el contenido del archivo usando la función print()
print(binary_data)