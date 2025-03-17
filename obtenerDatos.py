import yfinance as yf
import pandas as pd
from datetime import datetime
import pytz

# Zona horaria de Santiago de Chile
tz_santiago = pytz.timezone("America/Santiago")

# Obtener la hora actual en Santiago
hora_santiago = datetime.now(tz_santiago).time()

# Verificar si es después de las 17:00
# Si bien la bolsa de Santiago cierra a las 16:00, se da 1 hora más como extra por cualquier cosa.

if hora_santiago >= datetime.strptime("17:00:00", "%H:%M:%S").time():
    print(f"La bolsa ya cerró. Hora actual en Santiago: {hora_santiago.strftime('%H:%M:%S')}")

    # Obtener el precio de hoy
    data = yf.download("^IPSA", period="1d")
    price_today = data['Close'].iloc[0]
    ultimaFecha = data.index[-1].strftime("%Y-%m-%d")

    # Leer el archivo con los datos
    df = pd.read_csv("ipsaCompleto.csv")

    # Verificar si la última fecha de datos descargado NO está en el archivo.
    # Esto se hace para evitar escribir dos o más veces el mismo dato.
    if ultimaFecha not in df['Fecha'].values:
        
        # Si la fecha no existe, añadir el nuevo dato al final
        new_row = pd.DataFrame({'Fecha': [ultimaFecha], 'Valor IPSA': [round(price_today[0],2)]})
        df = pd.concat([df, new_row], ignore_index=True)

        # Guardar el DataFrame actualizado al archivo CSV
        df.to_csv('ipsaCompleto.csv', index=False)
        print(f"Nuevo dato agregado: {ultimaFecha} - {price_today[0]}")
    else:
        print(f"El dato de {ultimaFecha} ya está presente en el archivo.")

else:
    print(f"La bolsa sigue abierta. Hora actual en Santiago: {hora_santiago.strftime('%H:%M:%S')}")




