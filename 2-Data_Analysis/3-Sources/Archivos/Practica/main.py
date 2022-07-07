import funciones as f
import variables as v

# Cambiamos a la ruta de la carpeta a ordenar
f.ruta_dir(v.carpeta)

# Creamos las carpetas donde vamos a mover los archivos
f.crear_dirs(v.directorios)

# Mueve los archivos a la carpeta de su extension
f.mover_archivos(v.directorios, [v.doc_types, v.img_types, v.software_types])