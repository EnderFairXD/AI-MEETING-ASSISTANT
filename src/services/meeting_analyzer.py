import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate

load_dotenv()

def generate_meeting_minutes(transcript_text: str) -> str:
    """Envía la transcripción a Llama 3.1 para generar la minuta estructurada."""
    base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    
    # Subimos num_ctx a 16384 porque las transcripciones de reuniones largas
    # acumulan miles de palabras rápidamente.
    llm = Ollama(
        base_url=base_url,
        model="llama3.1",
        temperature=0.3,
        num_ctx=16384
    )
    
    template = """
    Eres un secretario ejecutivo de alto rendimiento experto en gestión corporativa. Analiza la siguiente transcripción de una reunión y genera una minuta oficial en Markdown perfectamente estructurada en español.

    La minuta DEBE incluir obligatoriamente las siguientes secciones:
    
    1. 📌 **Resumen Ejecutivo**: Un resumen de 3 o 4 líneas explicando el objetivo principal de la reunión y las conclusiones generales.
    2. 🤝 **Acuerdos y Decisiones Clave**: Una lista con viñetas de las decisiones más importantes que se aprobaron.
    3. 📋 **Plan de Acción / Lista de Tareas**: Genera una TABLA en Markdown con las tareas identificadas. La tabla debe tener las columnas: [Tarea | Responsable | Plazo]. Si no se menciona explícitamente un responsable o plazo, escribe "No especificado".
    4. ⏳ **Temas Pendientes**: Puntos que se hablaron pero cuya resolución se pospuso para futuras reuniones.

    Transcripción de la reunión:
    \"\"\"
    {transcripcion}
    \"\"\"
    """
    
    prompt = PromptTemplate(input_variables=["transcripcion"], template=template)
    chain = prompt | llm
    
    return chain.invoke({"transcripcion": transcript_text})