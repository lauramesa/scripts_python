from pytube import YouTube
import os
from moviepy.editor import *

# Ingresa el enlace de YouTube de la canción que deseas descargar
link = input("Ingresa el enlace de YouTube: ")
# Crea un objeto de YouTube con el enlace
video = YouTube(link)
# Filtra el objeto para obtener solo el audio de la canción
audio = video.streams.filter(only_audio=True).first()

# Descarga el archivo de audio en la carpeta actual
audio_file = audio.download()
# Extrae el nombre del archivo y cambia la extensión a .mp3
audio_file_name = os.path.splitext(audio_file)[0] + '.mp3'
# Convierte el archivo de audio a formato MP3 utilizando la librería moviepy
AudioFileClip(audio_file).write_audiofile(audio_file_name)

# Elimina el archivo de audio original
os.remove(audio_file)

print("Descarga completada!")