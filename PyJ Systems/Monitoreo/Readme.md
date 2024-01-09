# Script para Monitoreo

Simple script para monitoreo preventivo de alteración de archivos.

Dejarlo corriendo en un crontab:

```console
# m h  dom mon dow   command
*/30 * * * *  /path/check_and_mail.sh
```

Se debe modificar las variables del bash script __check_and_mail.sh__ con la ubicación del archivo maestro "md5sum.log" y del directorio dónde se encuentra los archivos a verificar.

**Importante**: debe existir un archivo "md5sum.log" con los hashes correctos.

## Simulación

En el caso particular del desafío el archivo que falla el MD5 es **"log.txt"**