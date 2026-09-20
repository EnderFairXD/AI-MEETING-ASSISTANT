import streamlit as st
import tempfile
import os
from utils.transcriber import transcribe_audio_file
from services.meeting_analyzer import generate_meeting_minutes

st.set_page_config(page_title="AI Meeting Assistant", page_icon="🎙️", layout="wide")

st.title("🎙️ Asistente Inteligente para Reuniones")
st.markdown("Sube el audio de tu reunión (MP3, WAV, M4A). El sistema transcribirá el audio localmente y generará la minuta oficial de forma privada.")

uploaded_audio = st.file_uploader("Sube el archivo de audio de la reunión", type=["mp3", "wav", "m4a"])

if uploaded_audio is not None:
    st.info("🎵 Archivo de audio cargado correctamente en el buffer de la app.")
    
    if st.button("🚀 Procesar Reunión Completa"):
        
        # Creamos contenedores visuales independientes para la transcripción y la minuta
        status_box = st.status("Iniciando flujo de procesamiento de audio...", expanded=True)
        
        try:
            # 🔧 TRUCO SENIOR: Guardar los bytes cargados en un archivo temporal en disco
            status_box.write("Guardando archivo de audio en directorio temporal de Linux...")
            with tempfile.NamedTemporaryFile(delete=False, suffix=f".{uploaded_audio.name.split('.')[-1]}") as tmp_file:
                tmp_file.write(uploaded_audio.read())
                tmp_path = tmp_file.name
            
            # Paso 1: Transcripción Local (Whisper)
            status_box.write("Iniciando transcriptor local Faster-Whisper (Extrayendo voz a texto)...")
            transcripcion_completa = transcribe_audio_file(tmp_path)
            
            # Limpieza inmediata del archivo temporal por seguridad y espacio
            os.unlink(tmp_path)
            
            if not transcripcion_completa.strip():
                status_box.update(label="Error en transcripción", state="error")
                st.error("No se pudo extraer ningún texto del audio. Asegúrate de que tenga voz audible.")
            else:
                # Paso 2: Análisis de Minuta (Ollama Llama 3.1)
                status_box.write("Audio transcrito con éxito. Enviando texto a Llama 3.1 en CasaOS para análisis conceptual...")
                minuta_final = generate_meeting_minutes(transcripcion_completa)
                
                status_box.update(label="¡Procesamiento de reunión completado!", state="complete")
                
                # Diseñar la interfaz en dos pestañas profesionales: Minuta y Transcripción Completa
                tab1, tab2 = st.tabs(["📋 Minuta Oficial de Reunión", "📝 Transcripción Completa (Logs)"])
                
                with tab1:
                    st.markdown("### 📋 Minuta Generada por IA")
                    st.download_button(
                        label="💾 Descargar Minuta (.md)",
                        data=minuta_final,
                        file_name="Minuta_Reunion.md",
                        mime="text/markdown",
                        key="btn_descarga_minuta"
                    )
                    st.markdown(minuta_final)
                    
                with tab2:
                    st.markdown("### 📝 Texto Transcrito por Whisper (Local)")
                    st.text_area("Historial con marcas de tiempo", transcripcion_completa, height=400, key="txt_area_transcripcion")
                    
        except Exception as e:
            status_box.update(label="Error crítico en el flujo", state="error")
            st.error(f"Error técnico del sistema: {str(e)}")

