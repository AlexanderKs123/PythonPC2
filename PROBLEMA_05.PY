
# Primero creamos la funcion que verifique la cantidad de veces que se usa dicho número en el dígito solicitado
def contar_digitos(numero, digito):
    # Convierte el número a una cadena para facilitar el manejo de dígitos
    numero_str = str(numero)

    # Usa el método count para contar la cantidad de veces que aparece el dígito
    cantidad = numero_str.count(str(digito))

    return cantidad

# ingresamos un número y su digito solicitado, por ejemplo el siguiente (puede ser modificado)
numero_ingresado = 333335000
digito_solicitado = 3

# En esta parte llamamos a dicha función y que nos muestre el resultado
resultado = contar_digitos(numero_ingresado, digito_solicitado)
print(f"Cantidad de veces {digito_solicitado} en el número {numero_ingresado}: {resultado}")