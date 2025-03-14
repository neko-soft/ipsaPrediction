import yfinance as yf
import pandas as pd
from datetime import datetime

# Obtén el precio de hoy
data = yf.download("^IPSA", period="1d")
price_today = data['Close'].iloc[0]

date_today = datetime.today().strftime('%Y-%m-%d')

# Carga tu archivo CSV
df = pd.read_csv("ipsaCompleto.csv")

# Verificar si la fecha actual ya existe en el DataFrame
if date_today not in df['Fecha'].values:
    # Si la fecha no existe, añadir el nuevo dato al final
    new_row = pd.DataFrame({'Fecha': [date_today], 'Valor IPSA': [round(price_today[0],2)]})
    df = pd.concat([df, new_row], ignore_index=True)

    # Guardar el DataFrame actualizado al archivo CSV
    df.to_csv('ipsaCompleto', index=False)
    print(f"Nuevo dato agregado: {date_today} - {price_today[0]}")
else:
    print(f"El dato de {date_today} ya está presente en el archivo.")