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

lista_hash = [
    ["90965b0eb20e68b7d0b59accd2a3b4fd", "copia.sh"],
    ["0b29406e348cd5f17c2fd7b47b1012f9", "log.txt"],
    ["6d5e43a730490d75968279b6adbd79ec", "pass.txt"],
    ["129ea0c67567301df1e1088c9069b946", "plan-A.txt"],
    ["4e9878b1c28daf4305f17af5537f062a", "plan-B.txt"],
    ["66bb9ec43660194bc066bd8b4d35b151", "script.py"]
]

for hashes, files in lista_hash:
    print(f"Hash: {hashes} | File: {files}")
    hash_md5 = calcular_md5sum(files)
    if hash_md5 == hashes:
        print("Data Integrity is Safe.")
    elif hash_md5 != hashes:
        print(f"""Data Integrity is not Safe.
              Expected Hash: {hashes}
              Current Hash: {hash_md5}""")