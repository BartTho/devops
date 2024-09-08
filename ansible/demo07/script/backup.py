#!/usr/bin/env python
import os
import shutil
import time

def backup_files(source_dir, backup_dir):
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    for filename in os.listdir(source_dir):
        source_file = os.path.join(source_dir, filename)
        backup_file = os.path.join(backup_dir, filename)
        shutil.copy(source_file, backup_file)
        print(f'Backed up: {source_file} to {backup_file}')

source_directory = "/home/bart/" # Change to your source directory
backup_directory = "/tmp" # Change to your backup directory
backup_files(source_directory, backup_directory)
time.sleep(1)