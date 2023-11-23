
# Esta función ( es_primo) toma un número como parámetro y utiliza un bucle for para verificar 

def es_numero_primo(numero):
    # En esta parte verificamos si el número es menor o igual a 1 (no es primo)
    if numero <= 1:
        return False

    # En esta parte verificamos divisibilidad por números desde 2 hasta la raíz cuadrada del número
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False  # El número no es primo si es divisible por algún número en este rango

    return True  # El número es primo si no fue divisible por ningún número en el rango

# Aqui insertamos el numero a verificar
numero = int(input("Ingrese un número para verificar si es primo: "))

if es_numero_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")