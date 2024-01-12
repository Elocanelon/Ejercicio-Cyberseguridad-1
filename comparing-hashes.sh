#!/bin/bash

# Definir los hashes MD5 originales
declare -A original_hashes=(
    ["copia.sh"]="90965b0eb20e68b7d0b59accd2a3b4fd"
    ["log.txt"]="0b29406e348cd5f17c2fd7b47b1012f9"
    ["pass.txt"]="6d5e43a730490d75968279b6adbd79ec"
    ["plan-A.txt"]="129ea0c67567301df1e1088c9069b946"
    ["plan-B.txt"]="4e9878b1c28daf4305f17af5537f062a"
    ["script.py"]="66bb9ec43660194bc066bd8b4d35b151"
)

# Función para calcular el hash MD5 de un archivo
calculate_md5() {
    local file="$1"
    md5sum "$file" | awk '{ print $1 }'
}

# Verificar la integridad de los archivos
for file in "${!original_hashes[@]}"; do
    original_hash="${original_hashes[$file]}"
    calculated_hash=$(calculate_md5 "$file")

    if [[ $calculated_hash == $original_hash ]]; then
        echo "El archivo $file no ha sido modificado. Hash: $calculated_hash"
    else
        echo "El archivo $file ha sido modificado. Hash original: $original_hash, Hash actual: $calculated_hash"
    fi
done

