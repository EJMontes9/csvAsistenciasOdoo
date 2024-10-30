import csv
from datetime import datetime, timedelta
import random


def generate_random_time(hour_start, hour_end, start_minute=0, end_minute=59):
    hour = random.randint(hour_start, hour_end)
    if hour == hour_start:
        minute = random.randint(start_minute, 59)  # Limitar minutos entre start_minute y 59
    elif hour == hour_end:
        minute = random.randint(0, end_minute)  # Limitar minutos entre 0 y end_minute
    else:
        minute = random.randint(0, 59)
    second = random.randint(0, 59)
    return hour, minute, second


def create_csv(start_date, end_date):
    header = ['Empleado', 'Entrada', 'Salida']
    rows = []

    # Nombre del empleado
    employee_name = "Nombre de la persona" #Nombre del empleado
    date_format = "%Y-%m-%d %H:%M:%S"

    # Conversión de la fecha de inicio y fin a objetos datetime
    start_date = datetime.strptime(start_date, "%d/%m/%Y")
    end_date = datetime.strptime(end_date, "%d/%m/%Y")

    current_date = start_date
    while current_date <= end_date:
        # Saltar sábados y domingos
        if current_date.weekday() in [5, 6]:
            current_date += timedelta(days=1)
            continue

        # Generar horas de entrada entre 7:30 y 8:30
        entry_hour, entry_minute, entry_second = generate_random_time(7, 8, start_minute=30, end_minute=59)

        # Generar horas de salida entre 18:00 y 18:59, con una pequeña probabilidad de ser entre 19:00 y 19:10
        exit_hour = random.choices([18, 19], weights=[0.9, 0.1])[0]
        if exit_hour == 18:
            exit_minute = random.randint(0, 59)
        else:
            exit_minute = random.randint(0, 10)
        exit_second = random.randint(0, 59)

        entry_time = current_date.replace(hour=entry_hour, minute=entry_minute, second=entry_second)
        exit_time = current_date.replace(hour=exit_hour, minute=exit_minute, second=exit_second)

        # Asegurarse de que la salida sea después de la entrada
        if exit_time < entry_time:
            exit_time += timedelta(hours=1)

        rows.append([
            employee_name,
            entry_time.strftime(date_format),
            exit_time.strftime(date_format)
        ])

        current_date += timedelta(days=1)

    with open('empleados_periodo_especifico.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)


# Fechas de inicio y fin especificadas
start_date = "05/09/2024"
end_date = "29/10/2024"  # Ajusta la fecha final a la actual si es necesario
create_csv(start_date, end_date)