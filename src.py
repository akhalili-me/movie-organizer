import re
import glob, os

def get_movie_info(movie):
    #Extract Year
    year_pattern = r'\b(?!1080\b)\d{4}\b'
    year = re.search(year_pattern,movie)
    year = year.group() if year else 'Not Found'

    #Extract Quality
    quality_pattern = r'\b(480p|720p|1080p)\b'
    quality = re.search(quality_pattern,movie)
    quality = quality.group() if quality else 'Not Found'
 
    return {'year': year, 'quality': quality}

#Deletes the extra stuff on movie/serie name
def name_fix(input):
    input = re.findall(r'\b[^._-]+\b', input)
    name = " ".join(input)
    movie_info = get_movie_info(name)
    
    year = movie_info.get("year")
    quality = movie_info.get("quality")
    
    if year != 'Not Found' or quality != 'Not Found':
        result = re.split(r'({}|{})'.format(year, quality), name, maxsplit=1)
        return ''.join(result[:2])
    
    return name
    
# Check for tv serie
def check_for_series(file):
    return bool(re.search("S..E..",file))

# Get all file names in a path
def get_all_file_names(path):
    os.chdir(path)
    files = []
    exts = ["*.mkv","*.mp4"]
    for ext in exts:
        files.extend(glob.glob(ext))
    return order_tv_movie(files)

def order_tv_movie(all_files):
    result = []
    for file in all_files:
        dic = {
            'name': file,
            'type': 'serie' if check_for_series(file) else 'movie'
        }
        result.append(dic)
    return result
    
def extract_name(file_name):
    fixed_name = name_fix(file_name)
    if check_for_series(fixed_name):
        return re.split(r'\bS..E..\b',fixed_name)[0].strip()

    return fixed_name






