from gtts import gTTS
import os

# El guion de nuestra "reunión ficticia"
texto_reunion = """
Buenos días equipo, gracias por asistir. 
El objetivo principal de esta breve reunión es organizar las tareas de esta semana. 
Javier, necesito que dejes configurado el servidor web para este viernes a más tardar.
Por otro lado, María, por favor encárgate de redactar el informe de métricas y envíalo mañana a primera hora.
Cualquier duda la revisamos por correo. Damos por concluida la sesión.
"""

print("Generando audio de prueba...")
# Convertir texto a voz en español
tts = gTTS(text=texto_reunion, lang='es', tld='es')
# Guardar como MP3
tts.save("reunion_prueba.mp3")

print("¡Listo! El archivo 'reunion_prueba.mp3' se ha creado en tu carpeta.")