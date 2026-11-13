# Asistente Inteligente para Reuniones

> **Este proyecto continúa en [suite-ia-local](https://github.com/EnderFairXD/suite-ia-local)**, que junta las cinco herramientas de IA local (contratos, documentación, correo, reuniones y estudio) con código común, tests y soporte para textos largos. Este repositorio queda archivado como referencia.

Aplicación de procesamiento de voz a texto y análisis semántico que funciona 100% en local. Permite transcribir audios de reuniones corporativas mediante `faster-whisper` (optimizada para CPU/RAM) y utilizar un LLM local (`Llama 3.1` vía Ollama) para estructurar el contenido en una minuta oficial, con resumen ejecutivo y tabla de tareas.

## Requisitos Previos
1. Instalar [Python 3.9+](https://www.python.org/)
2. Instalar [Ollama](https://ollama.com/) de forma local.
3. Descargar el modelo LLM: `ollama run llama3.1`

*(Nota: El modelo de transcripción `faster-whisper` de tamaño base se descargará de manera automática en el primer uso, ocupando aprox. ~150MB en disco).*

## Instalación y Despliegue
1. Clona el repositorio: `git clone <tu-enlace>`
2. Configura tu entorno virtual (`python -m venv .venv` y actívalo).
3. Instala las bibliotecas requeridas: `pip install -r requirements.txt`
4. Copia las variables de entorno base: `cp .env.example .env`
5. Arranca el servidor de la app: `streamlit run src/main.py`