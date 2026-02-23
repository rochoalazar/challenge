# Data Engineering Challenge - Stori

Este proyecto consiste en una solución de ingeniería de datos diseñada para ingerir, transformar y almacenar datos provenientes de una API de fútbol y un bucket de Amazon S3 de manera escalable y profesional.

## Arquitectura de la Solución
El proceso sigue un flujo de pipeline de datos modular:
1. [cite_start]**Ingesta:** Recolección incremental de datos de partidos vía API y metadatos de estadios desde S3[cite: 4, 5].
2. [cite_start]**Validación:** Verificación de presencia de datos en S3 antes de la ejecución (Bonus)[cite: 12].
3. [cite_start]**Transformación:** Enriquecimiento de datos, cálculo de métricas (total de goles) y normalización de campos[cite: 6, 7].
4. [cite_start]**Carga:** Almacenamiento de los datos transformados en una base de datos PostgreSQL local[cite: 5].
5. [cite_start]**Monitoreo:** Notificaciones automáticas a Slack en caso de fallos en el proceso (Bonus)[cite: 13].

## Requisitos Previos
* Python 3.x
* PostgreSQL instalado localmente
* [cite_start]Git [cite: 18]

## Instalación y Ejecución Local
1. Clonar el repositorio:
   ```bash
   git clone [https://github.com/rochoalazar/challenge.git](https://github.com/rochoalazar/challenge.git)
   cd challenge