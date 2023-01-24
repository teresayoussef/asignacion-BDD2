import pandas as pd
import matplotlib.pyplot as plt
import main

def estudiantes_mas_votados_por_la_comunidad(conexion, consulta) -> None:
    df = main.crear_dataframe(conexion, consulta)
    df = main.limpieza_datos(df)
    df = df.value_counts().reset_index(name='puntos')
    df = df.set_index('respuesta').head(15)
    df['puntos'].plot(kind='pie', subplots=True, autopct='%1.1f%%')
    plt.title('15 estudiantes elegidos por la comunidad ucabista')
    plt.show()