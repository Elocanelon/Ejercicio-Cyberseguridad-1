import os
import hashlib
import json


def generate_files_md5(path):
    new_hashes = {}
    for file in os.listdir(path):
        with open(f'{path}/{file}', 'rb') as f:
            bytes = f.read()
            md5_hash = hashlib.md5(bytes).hexdigest()
            new_hashes[file] = md5_hash
    return new_hashes


def compare_files_hashes(new_hashes, old_hashes):
    for file, md5_hash in new_hashes.items():
        if md5_hash == old_hashes[file]:
            print(
                f' Original: {old_hashes[file]} Generated: {new_hashes[file]} {file} OK')
        else:
            print(
                f' Original: {old_hashes[file]} Generated: {new_hashes[file]} {file} FAIL')


if __name__ == '__main__':
    path = 'PyJ Systems'
    new_hashes = generate_files_md5(path)
    old_hashes = json.load(open('old_hashes.json', 'r'))
    compare_files_hashes(new_hashes, old_hashes)
