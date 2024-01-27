import subprocess

files_md5 = [
    {
        "file": "copia.sh",
        "hash": "90965b0eb20e68b7d0b59accd2a3b4fd"
    },
    {
        "file": "log.txt",
        "hash": "0b29406e348cd5f17c2fd7b47b1012f9"
    },
    {
        "file": "pass.txt",
        "hash": "6d5e43a730490d75968279b6adbd79ec"
    },
    {
        "file": "plan-A.txt",
        "hash": "129ea0c67567301df1e1088c9069b946"
    },
    {
        "file": "plan-B.txt",
        "hash": "4e9878b1c28daf4305f17af5537f062a"
    },
    {
        "file": "script.py",
        "hash": "66bb9ec43660194bc066bd8b4d35b151"
    },
]

for file in files_md5:
    print(file["file"])
    command = 'md5sum -c <<< ' + "'" + file["hash"] + '  ' + file["file"] + "'"
    p = subprocess.Popen(command, shell=True, executable='/bin/bash')
    p.wait()
    if p.returncode == 0:
        print("Success\n")
    else:
        print("Error", p.returncode)
        print("")
