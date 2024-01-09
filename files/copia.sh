#!/bin/bash

# Configuración
source_directory="/ruta/del/directorio/a/copiar"
backup_directory="/ruta/del/directorio/de/copias/de/seguridad"
backup_filename="backup_$(date +'%Y%m%d_%H%M%S').tar.gz"

# Crear directorio de copias de seguridad si no existe
mkdir -p "$backup_directory"

# Crear copia de seguridad
tar -czvf "$backup_directory/$backup_filename" "$source_directory"

# Verificar si la copia de seguridad fue exitosa
if [ $? -eq 0 ]; then
    echo "Copia de seguridad exitosa. Archivo: $backup_filename"
else
    echo "Error al realizar la copia de seguridad."
fi
