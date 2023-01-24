import sqlite3
import pandas as pd
import preguntas.pregunta1 as p1
import preguntas.pregunta2 as p2
import preguntas.pregunta3 as p3
from consultas import pregunta1, pregunta2, pregunta3

def crear_dataframe(conexion, consulta):
    tabla = conexion.execute(consulta)
    columnas = [column[0] for column in tabla.description]
    df = pd.DataFrame.from_records(data=tabla.fetchall(), columns=columnas)
    return df

def limpieza_datos(df):
    df = df.apply(lambda x: x.str.lower() if x.dtype == "object" else x)
    df = df.dropna()
    for column in df.columns:
        df[column] = df[column].str.replace(r'\W', '', regex=True)
    for column in df.columns:
        df[column] = df[df[column].str.strip().astype(bool)] 
    return df

def main() -> None:
    conexion = sqlite3.connect('data/data.s3db')
    p1.obtener_respuestas(conexion, pregunta1.obtener_respuestas)
    p1.obtener_sexo_encuestados_EIU(conexion, pregunta1.obtener_sexo_encuestados_EIU)
    p1.obtener_sexo_encuestados_no_EIU(conexion, pregunta1.obtener_sexo_encuestados_no_EIU)
    p1.obtener_semestre_encuestados_EIU(conexion, pregunta1.obtener_semestre_encuestados_EIU)
    p1.obtener_semestre_encuestados_no_EIU(conexion, pregunta1.obtener_sexo_encuestados_no_EIU)
    p2.cualidades_EIU(conexion, pregunta2.cualidades_EIU)
    p3.estudiantes_mas_votados_por_la_comunidad(conexion, pregunta3.estudiantes_mas_votados_por_la_comunidad)


if __name__ == '__main__':
    main()