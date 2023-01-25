import pandas as pd
import matplotlib.pyplot as plt
import main

def obtener_respuestas(conexion, consulta):
    df = main.crear_dataframe(conexion, consulta)
    if len(df) > 0:
        df.groupby(['titulo']).size().plot(kind='bar', subplots=True)
        plt.title('Estudiantes que conocen el EIU')
        plt.show()
    else:
        pass

def obtener_sexo_encuestados_EIU(conexion, consulta):
    df = main.crear_dataframe(conexion, consulta)
    if len(df) > 0:
        df.groupby(['titulo']).size().plot(kind='pie', subplots=False, autopct='%1.1f%%')
        plt.title('Sexo de los encuestados que conocen el EIU')
        plt.show()
    else:
        pass

def obtener_sexo_encuestados_no_EIU(conexion, consulta):
    df = main.crear_dataframe(conexion, consulta)
    if len(df) > 0:
        df.groupby(['titulo']).size().plot(kind='pie', subplots=False, autopct='%1.1f%%')
        plt.title('Sexo de los encuestados que no conocen el EIU')
        plt.show()
    else:
        pass

def obtener_semestre_encuestados_EIU(conexion, consulta):
    df = main.crear_dataframe(conexion, consulta)
    if len(df) > 0:
        df.groupby(['titulo']).size().plot(kind='bar', subplots=True)
        plt.title('Semestre de estudiantes que conocen el EIU')
        plt.show()
    else: 
        pass

def obtener_semestre_encuestados_no_EIU(conexion, consulta):
    df = main.crear_dataframe(conexion, consulta)
    if len(df) > 0:
        df.groupby(['titulo']).size().plot(kind='bar', subplots=True)
        plt.title('Semestre de estudiantes que no conocen el EIU')
        plt.show()
    else:
        pass