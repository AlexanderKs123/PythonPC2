# Primero creamos una lista para almacenar los números ingresados
numeros_ingresados = []

# En esta parte iniciamos contadores para números pares e impares
pares = 0
impares = 0

# Creamos el Bucle while para permitir el ingreso de números
while True:
    respuesta = input("¿Desea ingresar un número? (SI/NO): ").upper()

    if respuesta == "NO":
        break  # Salir del bucle si la respuesta es NO
    elif respuesta == "SI":
        try:
            numero = int(input("Ingrese el número: "))
            numeros_ingresados.append(numero)

            # Aqui contamos números pares e impares
            if numero % 2 == 0:
                pares += 1
            else:
                impares += 1
        except ValueError:
            print("Por favor, ingrese un número válido.")

# En esta parte se imprime los resultados
print("Números ingresados:", numeros_ingresados)
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)