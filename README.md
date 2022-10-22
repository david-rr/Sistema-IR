# Sistema-IR
El sistema de recuperacion de información se basa en el modelo vectorial para determinar la informacion que debe recuperar dada una consulta.

Este sistema funciona con la coleccion de documentos y consultas cacm los cuales consisten en articulos y publicaciones pertenecientes a temas de computación en el idioma inglés.

#
La secuencia de ejecución debe ser:
1. procesar_docs.py
2. obtener_vocabularios.py
3. crear_matrices_frecuencias.py
4. calcular_similitud_cons_docs.py

Se debe respetar esta secuencia ya que cada uno de estos programas genera archivos que son utilizados en los siguientes lo que ayuda a aligerar la carga para no ejecutar siempre las mismas instrucciones iniciales.
