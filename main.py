import re
import datetime
import calendar

def validar_entrada(prompt, tipo_dato, validacion):
    """
    Función para validar la entrada del usuario.

    Args:
        prompt (str): Mensaje que se muestra al usuario para solicitar la entrada.
        tipo_dato (type): Tipo de dato esperado (str, int, etc.).
        validacion (callable): Función de validación que recibe el dato ingresado y devuelve True si es válido.

    Returns:
        dato: El dato ingresado por el usuario, convertido al tipo de dato especificado si es necesario.
    """
    while True:
        try:
            dato = input(prompt)
            if tipo_dato == str:
                return dato
            elif tipo_dato == datetime.date:
                return validar_fecha_nacimiento(dato)
            else:
                return tipo_dato(dato)
        except ValueError as e:
            print(f"¡Error! {e}")
        except Exception as e:
            print(f"¡Error inesperado! {e}")

def validar_fecha_nacimiento(prompt):
    """
    Función para validar la fecha de nacimiento del usuario.

    Args:
        prompt (str): Mensaje que se muestra al usuario para solicitar la entrada.

    Returns:
        fecha_nacimiento: Objeto `datetime.date` que representa la fecha de nacimiento válida.
    """
    while True:
        try:
            fecha_str = input(prompt)
            fecha_nacimiento = datetime.datetime.strptime(fecha_str, "%Y-%m-%d").date()
            # Validar que la fecha no sea en el futuro
            if fecha_nacimiento > datetime.date.today():
                raise ValueError("¡Fecha de nacimiento no válida! No puede ser en el futuro.")
            # Validar que la edad no sea superior a 120 años
            edad = calcular_edad(fecha_nacimiento)
            if edad > 120:
                raise ValueError("¡Edad no válida! No puede ser superior a 120 años.")
            return fecha_nacimiento
        except ValueError as e:
            print(f"¡Error! {e}")

def calcular_edad(fecha_nacimiento):
    """
    Función para calcular la edad en años a partir de una fecha de nacimiento.

    Args:
        fecha_nacimiento (datetime.date): Objeto `datetime.date` que representa la fecha de nacimiento.

    Returns:
        edad: La edad del usuario en años.
    """
    hoy = datetime.date.today()
    edad = hoy.year - fecha_nacimiento.year
    # Corregir la edad si el mes y/o día de nacimiento son posteriores a la fecha actual
    if (hoy.month < fecha_nacimiento.month) or \
       (hoy.month == fecha_nacimiento.month and hoy.day < fecha_nacimiento.day):
        edad -= 1
    return edad

print(f"Hola soy tu robot, antes de continuar primero necesito unos datos sencillos de ti.")

print(f"¿Estas seguro de que quieres continuar? (Escribe 'si' o 'no')")

response = input().lower()

if response == "si":
    nombre = validar_entrada("¿Cual es tu nombre? ", str, lambda x: x.isalpha())

    edad = validar_entrada("¿Cual es tu fecha de nacimiento? (YYYY-MM-DD): ", datetime.date, lambda x: True)

    año_nacimiento = edad.year
    mes_nacimiento = edad.month
    dia_nacimiento = edad.day

    print(f"Encantado de conocerte, {nombre}. Naciste el {dia_nacimiento} de {calendar.month_name[mes_nacimiento]} de {año_nacimiento}, lo que significa que tienes {calcular_edad(edad)} años.")
    print(f"¡Hasta pronto, {nombre}!")
else:
    print(f"Hasta luego!")
