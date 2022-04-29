import re
import glob, os

def extract_year(movie):
    #extract year
    all_nums = re.findall('[0-9]',movie)
    result = ''

    try:
        for i in range(4):
            result += all_nums[i]
    except:
        return ''

    if result != '1080':
        return result
    
    return ''


def extract_quality(movie):
    qualities = ['.*480p','.*720p','.*1080p']
    for q in qualities:
        q_output = re.findall(q,movie)

        if q_output:
            break

    if q_output != []:
        return q_output[0]

    return ''

# fix movie names
def name_fix(input):

    input = re.findall("[^._-]+",input)
    output = " ".join(input)

    # split from movie date
    year = extract_year(output)
    if year:
        result = re.findall('.*' + year,output)
        if result != []:
            return result[0]

    # split from movie quality
    result = extract_quality(output)
    if result:
        return result


    return output
  
# Check for tv series
def check_tv_series(movie_name):
    """
    Tv Series Check
    """

    result = re.findall("S..E..",movie_name)

    if result:
        return True
    else:
        return False

# Get all file names in a path
def get_all_file_names(path):
    os.chdir(path)

    files = []
    exts = ["*.mkv","*.mp4"]
    for ext in exts:
        files.extend(glob.glob(ext))
    
    result = order_tv_movie(files)
    return result



def order_tv_movie(all_files):
    """
    Order Tv and Movies
    """
    result = []


    for file in all_files:
        fixed_name = name_fix(file)

        if check_tv_series(fixed_name):
            dic = {
                'name': file,
                'type': 'serie'
            }
        else:
            dic = {
                'name': file,
                'type': 'movie'
            }
        
        result.append(dic)

    return result

    
# make directory 
def make_directory(dir):
    os.mkdir(dir)



def extract_series_name(serie_name):
    """
    Extract the series name
    """
    result = re.split("S..E..",serie_name)
    return result[0].strip()


def extract_name_date(movie_name):
    # Extract the date
    date = extract_year(movie_name)
    if date == '':
        return ''

    # fix movie name
    fixed_name = movie_name.split()
    fixed_name.pop()

    result = {'name': fixed_name,'date': date}
    return result







