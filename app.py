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














# for file in all_file_names:
#     if file['type'] == 'movie':
#         fixed_name = name_fix(file['name'])
#         folder_dir = main_dir / fixed_name
#         if not folder_dir.exists():
#             folder_dir.mkdir() 
#         if extract_name_date(fixed_name) != '':
#             print(f'Downloading subtitle for {fixed_name}...')
#             sub_url = get_movie_subtitle_url(fixed_name)
#             if sub_url != "Not Found":
#                 download_subtitle(sub_url,fixed_name)
#                 print('Done')
#                 print('-------------------------')
#                 sub_src = Path(parent_directory) / (fixed_name + '.zip')
#                 sub_src.rename(folder_dir / sub_src.name)
#             else:
#                 print('Subtitle Not Found')
#                 print('--------------------------')
#         movie_src = Path(parent_directory) / file['name']
#         movie_src.rename(folder_dir / movie_src.name)
#     if file['type'] == 'serie':
#         serie_name = name_fix(extract_series_name(file['name']))
#         serie_folder = main_dir / serie_name
#         serie_path = Path(parent_directory) / file['name']
#         if not serie_folder.exists():
#             serie_folder.mkdir() 
#         serie_path.rename(serie_folder / serie_path.name)
