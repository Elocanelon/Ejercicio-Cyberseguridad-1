# readData.py

`made by @ksreyr`

## Descripción

`readData.py` es un script de Python que compara los hashes MD5 de archivos para detectar cambios.

## Requisitos

- Python 3.x
- Script `fileToMd5.sh`
- Archivo `md5Backup.txt` con los hashes MD5 originales.

## Ejecución

1. Asegúrate de que `fileToMd5.sh` tenga permisos de ejecución y este en la carpeta que tiene lo archivos a analisar.
2. Ejecuta con `python3 readData.py` en la terminal.

## Interpretación de la Salida

- **Resultados de la comparación**:
  - **Common key-value pairs**: Archivos sin cambios en sus hashes MD5.
  - **Changed key-value pairs**: Archivos con hashes MD5 modificados.
