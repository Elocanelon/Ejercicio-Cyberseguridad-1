#!/bin/bash

declare -A files

#Files to check
files["copia.sh"]="90965b0eb20e68b7d0b59accd2a3b4fd"
files["log.txt"]="0b29406e348cd5f17c2fd7b47b1012f9"
files["pass.txt"]="6d5e43a730490d75968279b6adbd79ec"
files["plan-A.txt"]="129ea0c67567301df1e1088c9069b946"
files["plan-B.txt"]="4e9878b1c28daf4305f17af5537f062a"
files["script.py"]="66bb9ec43660194bc066bd8b4d35b151"

#Directory
dir="PyJ Systems"

for file in "$dir"/*
do
	name=$(echo "$file" | sed "s/$dir\///")
	md5_result=$(md5sum "$file" | cut -d' ' -f1)
	md5_expected="${files["$name"]}"

	echo '--------------------------------------------------------------'
	if [ "$md5_result" = "$md5_expected" ]; then
		echo "El archivo \"$file\" NO fue alterado."
	else
		echo "El archivo \"$file\" FUE ALTERADO."
		echo "Se esperaba el siguiente md5: $md5_expected"
		echo "se obtuvo el siguiente:       $md5_result"
	fi
done
echo '--------------------------------------------------------------'
