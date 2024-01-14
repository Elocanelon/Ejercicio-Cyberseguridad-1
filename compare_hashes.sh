#!/bin/bash

# Changing IFS from an space character to a jumpline character
IFS=$'\n'

# Declaring array of files to verify integrity
declare file_paths=( $(find $PWD/PyJ\ Systems -type f) )

# Declaring array of baseline hashes for comparison (this is an example it should be saved securely and not next to the files).
declare baseline_hashes=( $(cat $PWD/hashes.txt) )

# Looping through file_path array using wildcard @
for file_path in "${file_paths[@]}"
do
	md5hash_regex="\<$(md5sum "$file_path" | sed 's/\/.*\///g')\>"
	
	# Checking for errors during md5 hash generation	
	if [ $? -gt 0 ]
	then 
		echo "There was a problem generating the md5 hash"
		break
	fi


	# Regex patter matching using [[ ]] and =~ inside the if operation
	if [[ ${baseline_hashes[@]} =~ $md5hash_regex ]]
	then
		echo "File integrity verified and correct: $file_path"
	else
		echo "File tampered with: $file_path"
	fi
done			

