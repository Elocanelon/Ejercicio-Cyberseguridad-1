#Se definieron las variables faltantes:

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

# Define la ruta del archivo que deseas hashear
archivo_a_hash = r"c:\Users\MatiasXeneize\Desktop\HASH\PyJSystems\log.txt"

# Calcula el hash MD5 utilizando la función definida anteriormente
hash_md5 = calcular_md5sum(archivo_a_hash)

if hash_md5:
    print(f"El hash MD5 del archivo '{archivo_a_hash}' es: {hash_md5}")
