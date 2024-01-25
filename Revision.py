import hashlib
import pathlib

Files_Hashes = ["copia.sh","log.txt","pass.txt","plan-A.txt","plan-B.txt","script.py"]

OriginalHashes = ["90965b0eb20e68b7d0b59accd2a3b4fd", "0b29406e348cd5f17c2fd7b47b1012f9", 
                  "6d5e43a730490d75968279b6adbd79ec", "129ea0c67567301df1e1088c9069b946", "4e9878b1c28daf4305f17af5537f062a",
                  "66bb9ec43660194bc066bd8b4d35b151"]
a = 0

md5_hash_original = "90965b0eb20e68b7d0b59accd2a3b4fd"

with open("PyJ Systems\copia.sh","rb") as file_obj:
    file_contents = file_obj.read()
    md5_hash_new = hashlib.md5(file_contents).hexdigest()
    print(md5_hash_new)

if md5_hash_original == md5_hash_new:
    print("MD5 hash verified")
else:
    print("MD5 hash verification failed")

"""
for i in "PyJ Systems":
    md5_hash_original = OriginalHashes[a]
    a += 1

    with open(i,"rb") as file_obj:
        file_contents = file_obj.read()
        md5_hash_new = hashlib.md5(file_contents).hexdigest()
        print(md5_hash_new)
        
    if md5_hash_original == md5_hash_new:
        print("MD5 hash verified")
    else:
        print("MD5 hash verification failed")
"""