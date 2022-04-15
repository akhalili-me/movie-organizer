from src import *
import sub_download
from datetime import datetime
import shutil


        
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
        make_directory(folder_dir)

        # Moving the movie file
        movie_src = parent_directory +"/"+ file['name']
        shutil.move(movie_src,folder_dir)



    if file['type'] == 'serie':

        serie_name = name_fix(extract_series_name(file['name']))
        serie_folder = main_dir + "/" + serie_name
        serie_path = parent_directory + "/" + file['name']


        if os.path.exists(serie_folder) == False:
            make_directory(serie_folder) 
        
        shutil.move(serie_path,serie_folder)

