import re
import glob, os
import datetime as dt
import shutil




# fix movie names
def name_fix(input):

    result = re.findall("[^._]+",input)
    output = " ".join(result)

    qualities = ['.*480p','.*720p','.*1080p']
    for q in qualities:
        q_output = re.findall(q,output)

        if q_output:
            break

    if q_output != []:
        return q_output[0]

    return output
  

# Get all movie names in a path
def get_movie_names(path):
    os.chdir(path)

    files = []
    exts = ["*.mkv","*.mp4"]
    for ext in exts:
        files.extend(glob.glob(ext))
    
    return files

    
# make directory 
def make_directory(dir):
    os.mkdir(dir)





#App logic
parent_directory = input("Enter the parent directory: ")
main_dir = parent_directory +"/"+ dt.datetime.now().strftime('%Y-%m-%d')


if os.path.exists(main_dir) == False:
    make_directory(main_dir) 
    


all_movie_names = get_movie_names(parent_directory)
for movie in all_movie_names:

    #Creating movie directory
    fixed_name = name_fix(movie)
    folder_dir = main_dir + "/" + fixed_name
    make_directory(folder_dir)

    # Moving the movie file
    movie_src = parent_directory +"/"+ movie
    shutil.move(movie_src,folder_dir)








