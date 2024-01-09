#!/bin/bash

FILEMD5="/path/md5sum.log"
DIRMD5="/path/srv/files"

cd ${DIRMD5}

RESULT=$(md5sum  -c ${FILEMD5} | grep  FAILED)
CANT=$(echo ${RESULT}|wc -l )

if [ $CANT -ge "0" ]
then
        #echo ${RESULT}| mail -s "Te kakearon los archivos!" admin@example.org
        echo "URGENTE: Te kakearon los siguientes archivos:"
        echo ${RESULT}
fi
