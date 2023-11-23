
#Creamos la funcion obtener_numero_mes 

def obtener_numero_mes(mes):
    meses = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]

    # En esta parte devuelvemos el número de mes correspondiente
    return str(meses.index(mes) + 1).zfill(2)

def convertir_fecha(fecha):
    # Aqui verificamos si la fecha está en formato mes-día-año
    if '/' in fecha:
        partes = fecha.split('/')
        mes_numero, dia_numero, año_numero = partes[0].zfill(2), partes[1].zfill(2), partes[2]
    else:  # La fecha está en formato de texto
        partes = fecha.split()
        mes_numero = obtener_numero_mes(partes[0])
        dia_numero = partes[1].zfill(2)
        año_numero = partes[2]

    # En esta parte formateamps la fecha en AAAA-MM-DD
    fecha_formateada = f"{año_numero}-{mes_numero}-{dia_numero}"

    return fecha_formateada

# Aqui ingresamos el formato mes-día-año o texto
fecha_input = input("Ingrese una fecha en formato mes-día-año o texto (ejemplo: 9/8/1636 o Septiembre 8, 1636): ")

fecha_convertida = convertir_fecha(fecha_input)
print(f"Fecha convertida: {fecha_convertida}")