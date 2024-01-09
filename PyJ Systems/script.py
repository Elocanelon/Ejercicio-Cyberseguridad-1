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

#La funcion calcular_md5sum solicita como parámetro, ruta_archivo, y tamano_bloque el cual ya tiene asignado 65536 por defecto
# En el if del final, en caso de existir hash_md5, nos imprime el archivo y su hash. Para eso hay que darle un valor a archivo_a_hash
# con el path y el archivo a hashear, y por otro lado a hash_md5 le damos el valor que nos devuelva la funcion al hashear el archivo.
# Luego de chequear uno por uno, he visto que unicamente el log.txt difiere con los has que se encuentran en la consigna
# dando por hecho que ha sido el archivo alterado en cuestión.
archivo_a_hash = "log.txt" 
hash_md5 = calcular_md5sum(archivo_a_hash)

if hash_md5:
    print(f"El hash MD5 del archivo '{archivo_a_hash}' es: {hash_md5}")
