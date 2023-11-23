
# Primero inicializamos los dos primeros números de la serie de Fibonacci
fibonacci_1, fibonacci_2 = 0, 1

print(fibonacci_1)

# Por ultimo generamos la serie de Fibonacci hasta el número 50 respectivamente
while fibonacci_2 <= 50:
    print(fibonacci_2)
    fibonacci_1, fibonacci_2 = fibonacci_2, fibonacci_1 + fibonacci_2