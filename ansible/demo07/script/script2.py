import shutil
source_folder = '/etc/passwd'
backup_folder = '/home/bart/passwd'

shutil.copytree(source_folder, backup_folder)