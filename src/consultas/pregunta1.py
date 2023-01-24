obtener_respuestas = '''
    SELECT Opcion.titulo
    FROM Respuesta
    INNER JOIN Opcion ON Respuesta.num_pregunta = Opcion.num_pregunta
    AND Respuesta.num_opcion = Opcion.num_opcion
    AND Respuesta.num_pregunta = 4;
'''

obtener_sexo_encuestados_EIU = '''
    SELECT t1.num_encuesta, t2.titulo
    FROM (
        SELECT *
        FROM Respuesta
        WHERE num_pregunta = 4
        AND num_opcion = 1
    ) t1
    INNER JOIN (
        SELECT Respuesta.num_encuesta, Opcion.titulo
        FROM Respuesta
        INNER JOIN Opcion
        ON Respuesta.num_pregunta = Opcion.num_pregunta
        AND Respuesta.num_opcion = Opcion.num_opcion
        AND Respuesta.num_pregunta = 1
    ) t2
    ON t1.num_encuesta = t2.num_encuesta;
'''

obtener_sexo_encuestados_no_EIU = '''
    SELECT t1.num_encuesta, t2.titulo
    FROM (
        SELECT *
        FROM Respuesta
        WHERE num_pregunta = 4
        AND num_opcion = 2
    ) t1
    INNER JOIN (
        SELECT Respuesta.num_encuesta, Opcion.titulo
        FROM Respuesta
        INNER JOIN Opcion
        ON Respuesta.num_pregunta = Opcion.num_pregunta
        AND Respuesta.num_opcion = Opcion.num_opcion
        AND Respuesta.num_pregunta = 1
    ) t2
    ON t1.num_encuesta = t2.num_encuesta;
'''

obtener_semestre_encuestados_EIU = '''
    SELECT t1.num_encuesta, t2.titulo
    FROM (
        SELECT *
        FROM Respuesta
        WHERE num_pregunta = 4
        AND num_opcion = 1
    ) t1
    INNER JOIN (
        SELECT Respuesta.num_encuesta, Opcion.titulo
        FROM Respuesta
        INNER JOIN Opcion
        ON Respuesta.num_pregunta = Opcion.num_pregunta
        AND Respuesta.num_opcion = Opcion.num_opcion
        AND Respuesta.num_pregunta = 2
    ) t2
    ON t1.num_encuesta = t2.num_encuesta;
'''

obtener_semestre_encuestados_no_EIU = '''
    SELECT t1.num_encuesta, t2.titulo
    FROM (
        SELECT *
        FROM Respuesta
        WHERE num_pregunta = 4
        AND num_opcion = 2
    ) t1
    INNER JOIN (
        SELECT Respuesta.num_encuesta, Opcion.titulo
        FROM Respuesta
        INNER JOIN Opcion
        ON Respuesta.num_pregunta = Opcion.num_pregunta
        AND Respuesta.num_opcion = Opcion.num_opcion
        AND Respuesta.num_pregunta = 2
    ) t2
    ON t1.num_encuesta = t2.num_encuesta;
'''