# Primero creamos una lista para almacenar los datos de los alumnos
lista_alumnos = []

# En esta parte solicitamos la cantidad de alumnos que deseamos ingresar
numero_alumnos = int(input("Ingrese la cantidad de alumnos: "))

# Creamos un bucle para ingresar datos de cada alumno
for _ in range(numero_alumnos):
    # Solicitar el nombre del alumno
    nombre_alumno = input("Ingrese el nombre del alumno: ")

    # Creamos una lista para almacenar las calificaciones del alumno
    calificaciones = []

    # Creamos un bucle para ingresar las calificaciones del alumno
    for i in range(3):
        calificacion = float(input(f"Ingrese la calificación {i+1} para {nombre_alumno}: "))
        calificaciones.append(calificacion)

    # Aqui hacemos el uso del uso de un diccionario 
    alumno = {"Alumno": nombre_alumno, "Notas": calificaciones}
    lista_alumnos.append(alumno)

# En esta ultima parte se imprime el listado completo de alumnos
print("\nListado de Alumnos:")
for alumno in lista_alumnos:
    print(alumno)