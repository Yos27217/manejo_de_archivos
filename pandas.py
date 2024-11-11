import pandas as pd

# Crear un DataFrame vacío y agregar datos
data = {
    'Nombre': ['Juan', 'Maria', 'Luis'],
    'Edad': [25, 30, 35],
    'Salario': [5000, 6000, 7000]
}

df = pd.DataFrame(data)

# Agregar una nueva columna calculada
df['Salario_Dobrado'] = df['Salario'] * 2

# Guardar el DataFrame en un archivo Excel
df.to_excel('persona.xlsx', index=False)

print("Archivo Excel generado con éxito.")