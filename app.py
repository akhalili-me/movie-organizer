from src import *
import sub_download
from datetime import datetime
from shutil import move
from sub_download import *
from pathlib import Path

        
parent_directory = input("Enter the parent directory: ")
main_dir = parent_directory +"/"+ datetime.now().strftime('%Y-%m-%d')


if os.path.exists(main_dir) == False:
    make_directory(main_dir) 
    


all_file_names = get_all_file_names(parent_directory)
for file in all_file_names:

    if file['type'] == 'movie':
        #Creating movie directory
        fixed_name = name_fix(file['name'])
        folder_dir = main_dir + "/" + fixed_name

        if os.path.exists(folder_dir) == False:
            make_directory(folder_dir) 

        # Downloading subtitle
        if extract_name_date(fixed_name) != '':

            print('Downloading subtitle for ' + fixed_name +'...')

            sub_url = get_movie_subtitle_url(fixed_name)
            if sub_url != "Not Found":
                download_subtitle(sub_url,fixed_name)
                print('Done')
                print('-------------------------')
                # Moving subtitle
                sub_src = parent_directory + "/"+ fixed_name + '.zip'
                move(sub_src,folder_dir)
            else:
                print('Subtitle Not Found')
                print('--------------------------')
                
        # Moving the movie file
        movie_src = parent_directory +"/"+ file['name']
        move(movie_src,folder_dir)



    if file['type'] == 'serie':

        serie_name = name_fix(extract_series_name(file['name']))
        serie_folder = main_dir + "/" + serie_name
        serie_path = parent_directory + "/" + file['name']


        if os.path.exists(serie_folder) == False:
            make_directory(serie_folder) 
        
        move(serie_path,serie_folder)

