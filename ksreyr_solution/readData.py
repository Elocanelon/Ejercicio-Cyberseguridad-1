import subprocess

# Path to the backup file with the original MD5 hashes
backup_file_path = 'md5Backup.txt'
original_hashes = {}
current_hashes = {}

# Path to the shell script that generates current MD5 hashes
script_path = './fileToMd5.sh'

result = subprocess.run([script_path], stdout=subprocess.PIPE, text=True)

for line in result.stdout.splitlines():
    file_name, md5_hash = line.strip().split(' ', 1)
    current_hashes[file_name.rstrip(':')] = md5_hash


with open(backup_file_path, 'r') as file:
    for line in file:
        md5_hash, file_name = line.strip().split(' ', 1)
        original_hashes[file_name] = md5_hash


# Compare the current hashes with the original hashes to find common and changed pairs
common_pairs = {k: original_hashes[k] for k in original_hashes if k in current_hashes and original_hashes[k] == current_hashes[k]}
changed_files = {k: original_hashes[k] for k in original_hashes if k in current_hashes and original_hashes[k] != current_hashes[k]}

print("Common key-value pairs:", common_pairs)
print("Changed key-value pairs:", changed_files)
