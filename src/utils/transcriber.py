import os
from faster_whisper import WhisperModel

def transcribe_audio_file(file_path: str) -> str:
    """
    Carga el modelo Whisper localmente en la CPU, procesa el archivo 
    de audio y devuelve la transcripción con marcas de tiempo.
    """
    # Inicializamos el modelo optimizado para CPU en modo INT8
    # Tamaños disponibles: tiny, base, small, medium, large-v3
    model = WhisperModel("base", device="cpu", compute_type="int8")
    
    # Ejecutamos la transcripción forzando el idioma español
    segments, info = model.transcribe(file_path, beam_size=5, language="es")
    
    transcript_text = ""
    
    # Recorremos los segmentos de audio procesados
    for segment in segments:
        # Formateamos con marcas de tiempo estilo: [00:12 -> 00:15]: Hola a todos.
        start_min = int(segment.start // 60)
        start_sec = int(segment.start % 60)
        end_min = int(segment.end // 60)
        end_sec = int(segment.end % 60)
        
        transcript_text += f"[{start_min:02d}:{start_sec:02d} -> {end_min:02d}:{end_sec:02d}]: {segment.text}\n"
        
    return transcript_text