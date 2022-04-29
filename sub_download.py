import requests
import re
import src


def download_subtitle(url,name):
    page = requests.get(url).text

    file = re.findall("https.*.zip",page)
    if file == []:
        file = re.findall("https.*.rar",page)

    d_file = requests.get(file[0])

    open(name + '.zip', 'wb').write(d_file.content)



def get_movie_subtitle_url(movie_name):
    # Search for movie
    movie = src.extract_name_date(movie_name)
    static_search_query = "https://worldsubtitle.site/?s="
    movie_url = "+".join(movie['name'])
    search_query = static_search_query + movie_url

    page = requests.get(search_query).text
    pattern = "https.*-" + movie['date'] + "/"
    url = re.findall(pattern,page)

    if url != []:
        return url[0]

    return 'Not Found'



