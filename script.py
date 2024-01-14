# Script para generar hash md5

import hashlib

def calcular_md5sum(ruta_archivo, tamano_bloque=65536):
    md5 = hashlib.md5()
    try:
        with open(ruta_archivo, 'rb') as archivo:
            for bloque in iter(lambda: archivo.read(tamano_bloque), b''):
                md5.update(bloque)
        return md5.hexdigest()
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta_archivo}' no se encontró.")
        return None
    except Exception as e:
        print(f"Error al calcular el hash MD5: {e}")
        return None

# Se asignan valores a las variables que se hacen mencion en la condicion, y se coloca manualmente cada archivo
archivo_a_hash = ".\PyJ Systems\log.txt"
hash_md5 = calcular_md5sum(archivo_a_hash)

if hash_md5:
    print(f"El hash MD5 del archivo '{archivo_a_hash}' es: {hash_md5}")
# El resultado arroja al hash del archivo y se compara con el dado en el ejercicio
