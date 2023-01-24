import pandas as pd
import matplotlib.pyplot as plt
import main

def cualidades_EIU(conexion, consulta):
    df = main.crear_dataframe(conexion, consulta)
    df = main.limpieza_datos(df)
    df.groupby(['respuesta']).size().plot(kind='pie', autopct='%1.1f%%')
    plt.title('Cualidades de estudiantes que conocen el EIU')
    plt.show()