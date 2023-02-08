import requests
from src import *
from bs4 import BeautifulSoup


def make_soup(url):
    response = requests.get(url).text
    return BeautifulSoup(response,'html.parser')



def get_file_subtitle_url(file):
    file_name = extract_name(file)
    url = 'https://worldsubtitle.me/?s=' + file_name.replace(' ', '+')
    soup = make_soup(url)

    posters = soup.find_all('div', class_='cat-post-tmp')
    for div in posters:
        a_tag = div.find('a')
        if a_tag['title'] == file_name:
            return a_tag['href']

def download_subtitle(url, path):
    soup = make_soup(url)
    subtitles = soup.find_all('div', class_='new-link-3')

    sub_urls = [item.find('a')['href'] for item in subtitles]

    for sub in sub_urls:
        response = requests.get(sub)

        file_name = sub.split("/")[-1]
        file_path = os.path.join(path, file_name)

        with open(file_path, "wb") as f:
            f.write(response.content)

