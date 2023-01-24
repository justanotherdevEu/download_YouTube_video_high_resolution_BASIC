from pytube import YouTube   #   RECUERDA que es necesario ejecutar en la CMD  "pip install pytube" para que se instale en Windows el paquete de Python (librería)
import os
link = input("Introduce el enlace del vídeo de YouTube que quieras descargar:\t ")
yt = YouTube(link)
video_HD = yt.streams.get_highest_resolution()
video_HD.download()
#https://stackoverflow.com/questions/62894380/download-full-hd-youtube-video-in-python
                #ahora un código que hice que por mucho que esté bien hecho, no hace caso la terminal pues descarga en vídeo donde quiere
"""destino = input("\n\t\tQuieres descargarlo en C: o en D:?\n\t\t1 para C: y 2 para D:\t :")
destino = int(destino)
while  destino != 2 and destino != 1:
    print("\n\n\tOye, tienes que meter 1 o 2 y ENTER")
    destino = input("\n\t\tQuieres descargarlo en C: o en D:?")
    destino = int(destino)
if destino == 1:
    os.system("C:")
    for a in range(25):
        os.system("cd ..") # unas 25 veces por si estoy en alguna carpeta muy profunda
elif destino == 2:
    os.system("D:")
    for a in range(25):
        
        os.system("cd ..") # unas 25 veces por si estoy en alguna carpeta muy profunda"""