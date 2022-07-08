import os
import shutil

class Fichero:

    def __init__(self, carpeta, extensiones = None, ruta = os.getcwd()):
        self.carpeta = carpeta
        self.extensiones = extensiones
        self.ruta = ruta
        self.ruta_dir()
        self.crear_directorio()
        self.mover_archivo()

    def ruta_dir(self):
        os.chdir(self.ruta)

    def crear_directorio(self):
        os.makedirs(self.carpeta, exist_ok=True)
    
    def mover_archivo(self):
        for archivo in os.listdir():
            if os.path.isdir(os.path.join(os.getcwd(), archivo)):
                print(archivo, "es una carpeta")
            else:
                if self.extensiones == None or archivo.endswith(self.extensiones):
                    shutil.move(archivo, self.carpeta)