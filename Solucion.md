Solucion Reto Ciberseguridad 1

Luego de realizar una primera ejecución con MD5sum para extraer el ultimo hash de cada uno de los archivos. Entre todos ellos, el unico que presenta un cambio es el archivo "log.txt", donde se encuentra que el hash inicial era 0b29406e348cd5f17c2fd7b47b1012f9 y, posterior a su revisión, se encuentra el cambio al Hash *f2b0428b975452afbc641e46a042231b*

MD5sums de los archivos

90965b0eb20e68b7d0b59accd2a3b4fd  copia.sh
f2b0428b975452afbc641e46a042231b  log.txt
6d5e43a730490d75968279b6adbd79ec  pass.txt
129ea0c67567301df1e1088c9069b946  plan-A.txt
4e9878b1c28daf4305f17af5537f062a  plan-B.txt
66bb9ec43660194bc066bd8b4d35b151  script.py

Hash originales

90965b0eb20e68b7d0b59accd2a3b4fd  copia.sh
<font color="red">0b29406e348cd5f17c2fd7b47b1012f9  log.txt</font>
6d5e43a730490d75968279b6adbd79ec  pass.txt
129ea0c67567301df1e1088c9069b946  plan-A.txt
4e9878b1c28daf4305f17af5537f062a  plan-B.txt
66bb9ec43660194bc066bd8b4d35b151  script.py