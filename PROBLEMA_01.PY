# En esta parte inicializamos una lista para almacenar los numeros divisible por 7 y múltiplo de 5
resultados_7_5 = []

# En esta parte iteramos a través del rango de 1500 a 2700 
for numero in range(1500, 2701):
    # Verificamos si el número es divisible por 7 y múltiplo de 5
    if numero % 7 == 0 and numero % 5 == 0:
        # En esta parte se agraga a la lista de resultados, si cumplen ambas condiciones
        resultados_7_5.append(numero)

print("Números divisibles por 7 y múltiplos de 5 en el rango de 1500 a 2700:")
print(resultados_7_5)