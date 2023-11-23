
# Creamos la funcion factorial 
def factorial(numero):
    # En esta parte verificamos si el número es 0 o 1, en cuyo caso el factorial es 1
    if numero == 0 or numero == 1:
        return 1
    else:
        # En esta parte calculamos el factorial utilizando un bucle
        resultado = 1
        for i in range(2, numero + 1):
            resultado *= i
        return resultado

# Aqui ingresamos el numero para calcular su factorial
numero = int(input("Ingrese un número para calcular su factorial: "))

resultado_factorial = factorial(numero)
print(f"El factorial de {numero} es: {resultado_factorial}")