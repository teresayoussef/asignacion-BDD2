import pandas as pd
import matplotlib.pyplot as plt
import squarify 
import main

def cualidades_EIU(conexion, consulta):
    df = main.crear_dataframe(conexion, consulta)
    df = main.limpieza_datos(df)
    if len(df) > 0:
        df = df.groupby(['respuesta']).size().reset_index(name='counts')
        squarify.plot(label=df['respuesta'], sizes=df['counts'], alpha=.7)
        plt.show()
        plt.title("Cualidades del EIU")
    else: 
        pass
