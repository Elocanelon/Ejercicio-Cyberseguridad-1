Tras mucho estudio y dedicacion lograste conseguir tu primer trabajo en ciberseguridad, haciendo monitoreo de actividades en la red de la empresa PyJ Systems. 

En una de las revisiones descubres que hubo un acceso no autorizado a una de las carpetas que contenia informacion confidencial de la empresa, de acuerdo a las politicas de seguridad de la empresa se tiene que evaluar la disponibilidad, confidencialidad e integridad de los archivos que hay dentro de la carpeta. 

Durante las evaluaciones se verifico que la informacion sigue disponible y confiencial, por lo que es necesario verificar que la informacion de la empresa siga integra por lo que te asignan ese valor. 

De acuerdo a los ultimas revisiones de las normativas y politicas de seguridad, estos son los hash md5 de los archivos 

90965b0eb20e68b7d0b59accd2a3b4fd  copia.sh
0b29406e348cd5f17c2fd7b47b1012f9  log.txt
6d5e43a730490d75968279b6adbd79ec  pass.txt
129ea0c67567301df1e1088c9069b946  plan-A.txt
4e9878b1c28daf4305f17af5537f062a  plan-B.txt
66bb9ec43660194bc066bd8b4d35b151  script.py

Revisa si algun archivo fue alterado durante el ultimo ataque y de existir ¿cual seria?

Se utilizaron dos métodos:

1. Utilizando el comando md5sum en la terminal se obtiene el hash de cada archivo y se comparó con el dado en el ejercicio, dando como resultado que el archivo log.txt fue modificado y/o alterado.
el hash resultante de log.txt es f2b0428b975452afbc641e46a042231b

2. Utilizando el script que indica el ejercicio, se obtuvo el mismo resultado.