import yfinance as yf
import pandas as pd
from datetime import datetime

# Obtén el precio de hoy
data = yf.download("^IPSA", period="1d")
price_today = data['Close'].iloc[0]

ultimaFecha = data.index[-1].strftime("%Y-%m-%d")

# Carga tu archivo CSV
df = pd.read_csv("ipsaCompleto.csv")

# Verificar si la fecha actual ya existe en el DataFrame
if ultimaFecha not in df['Fecha'].values:
    # Si la fecha no existe, añadir el nuevo dato al final
    new_row = pd.DataFrame({'Fecha': [ultimaFecha], 'Valor IPSA': [round(price_today[0],2)]})
    df = pd.concat([df, new_row], ignore_index=True)

    # Guardar el DataFrame actualizado al archivo CSV
    df.to_csv('ipsaCompleto.csv', index=False)
    print(f"Nuevo dato agregado: {ultimaFecha} - {price_today[0]}")
else:
    print(f"El dato de {ultimaFecha} ya está presente en el archivo.")