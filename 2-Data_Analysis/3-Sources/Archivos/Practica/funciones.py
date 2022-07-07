import os
import shutil

def ruta_dir(carpeta):
    # Definir el punto de partida
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # Cambiamos la ruta a la carpeta que vamos a ordenar
    os.chdir(os.getcwd() + '\\'+ carpeta)

def crear_dirs(directorios):
    for dir in directorios:
        os.makedirs(dir, exist_ok=True)

def mover_archivos(directorios, extensiones):
    for archivo in os.listdir():
        if os.path.isdir(os.path.join(os.getcwd(), archivo)):
            print(archivo, "es una carpeta")
        else:
            if archivo.endswith(extensiones[0]):
                print(archivo, "es un documento")  
                shutil.move(archivo, directorios[0])
            elif archivo.endswith(extensiones[1]):
                print(archivo, "es una imagen") 
                shutil.move(archivo, directorios[1]) 
            elif archivo.endswith(extensiones[2]):
                print(archivo, "es un software")
                shutil.move(archivo, directorios[2])
            else:
                print(archivo, "es otro")
                shutil.move(archivo, directorios[3])