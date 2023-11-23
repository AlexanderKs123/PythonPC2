# Número de filas en el patrón 
numero_filas = 5

# Se muestra la parte superior del patrón
for i in range(1, numero_filas + 1):
    print('* ' * i)

# Se muestra la parte inferior del patrón
for i in range(numero_filas - 1, 0, -1):
    print('* ' * i)