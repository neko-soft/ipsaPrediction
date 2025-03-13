# Este script es sólamente para odenar los datos dentro de la carpeta ./datosHistoricos/


import pandas as pd
import os

def cargar_datos(directorio):
    archivos = [f for f in os.listdir(directorio) if f.endswith(('.csv', '.xlsx'))]
    datos = []

    for archivo in archivos:
        ruta = os.path.join(directorio, archivo)
        if archivo.endswith('.csv'):
            df = pd.read_csv(ruta)
        elif archivo.endswith('.xlsx'):
            df = pd.read_excel(ruta)
        else:
            continue
        datos.append(df)

    df_final = pd.concat(datos, ignore_index=True)
    return df_final

directorio = "datos"
df = cargar_datos(directorio)
df.to_csv("ipsa_unificado.csv", index=False)
print("Datos unificados guardados en ipsa_unificado.csv")
