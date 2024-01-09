#!/bin/bash

while read -r line; 
do echo "$line" | md5sum -c ;
done < input
