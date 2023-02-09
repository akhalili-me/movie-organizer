from datetime import datetime
from pathlib import Path
from sub_download import *
from src import *
import shutil

parent_directory = input("Enter the parent directory: ")
main_dir = Path(parent_directory) / datetime.now().strftime('%Y-%m-%d')
if not main_dir.exists():
    main_dir.mkdir() 

all_file_names = get_all_file_names(parent_directory)

for file in all_file_names:
    fixed_name = extract_name(file['name'])
    new_file_dir = main_dir / fixed_name
    current_file_dir = Path(parent_directory) / file['name']

    # moving the file to the new dir
    if not new_file_dir.exists():
        new_file_dir.mkdir() 
    shutil.move(current_file_dir,new_file_dir)

    #download subtitle
    print(f'Downloading subtitle for {fixed_name}...')
    url = get_url(file['name'])
    download_subtitle(url,new_file_dir),print('Done') if url != None else print('Subtitle failed to download')
    print('-------------------------')
