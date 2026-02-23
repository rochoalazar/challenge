# Challenge Data Engineering 

Pipeline de datos (ETL) diseñado para procesar información de partidos y estadios mediante la integración de APIs externas, Amazon S3 y PostgreSQL.

## Flujo del Proyecto
1. **Generación:** Datos de una API abierta llamada jsonplaceholder
2. **Ingesta:** Código en Python para hacer el request y la libreria boto3 para S3 
2. **Resiliencia:** Manejo de errores y validación de archivos en S3. En ausencia de credenciales de AWS, el sistema utiliza un respaldo de datos locales para asegurar la continuidad del pipeline.
3. **Transformación:** Cruce de datasets (Merge), cálculo de métricas de desempeño (goles totales) y normalización de esquemas.
4. **Carga:** Ingesta automatizada en base de datos PostgreSQL.
5. **Notificaciones:** Integración con Slack para alertar sobre fallos en el proceso. (Al no contar con una cuenta en Slack el mensaje es simulado)

## Requisitos
* Python 3.10+
* PostgreSQL
* Boto3, Pandas, SQLAlchemy, requests, etc.

## Ejecución
1. Clonar el repositorio:
   ```bash
   git clone [https://github.com/rochoalazar/challenge.git](https://github.com/rochoalazar/challenge.git)
   cd challenge
Instalar dependencias:

   Bash
   pip install -r requirements.txt
   Ejecutar el pipeline:

   Bash
   python main.py

---
