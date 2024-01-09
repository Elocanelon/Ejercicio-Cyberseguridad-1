#!/bin/bash

ls -A1 | while IFS= read -r file; do
    echo "$file: $(md5 -q "$file")"
done

