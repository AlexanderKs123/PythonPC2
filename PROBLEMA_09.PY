
# Primero creamos la funcion omitir_vocales 

def omitir_vocales(cadena):
    # En esta parte creamos una cadena sin vocales
    cadena_sin_vocales = ''.join(caracter for caracter in cadena if caracter.lower() not in 'aeiou')

    return cadena_sin_vocales

# Aqui ingresamos la cadena de texto
entrada_usuario = input("Ingrese una cadena de texto: ")

# Se muestra el resultado sin vocales
resultado = omitir_vocales(entrada_usuario)
print(f"Texto sin vocales: {resultado}")