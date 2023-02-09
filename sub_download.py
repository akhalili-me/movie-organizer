import requests
from src import *
from bs4 import BeautifulSoup
import os

def make_soup(url):
    response = requests.get(url).text
    return BeautifulSoup(response,'html.parser')

def get_url(file):
    file_name = extract_name(file)
    url = 'https://worldsubtitle.me/?s=' + file_name.replace(' ', '+')
    soup = make_soup(url)

    posters = soup.find_all('div', class_='cat-post-tmp')
    for div in posters:
        a_tag = div.find('a')
        if a_tag['title'].lower() == file_name.lower():
            return a_tag['href']

def download_subtitle(url,path):
    soup = make_soup(url)
    subtitles = soup.find_all('div', class_='new-link-3')
    
    sub_urls = []
    for item in subtitles:
        a_tag = item.find('a')
        if a_tag:
            sub_urls.append(a_tag.get("href"))

    for subtitle_url in sub_urls:
        file_name = subtitle_url.split("/")[-1]
        file_path = os.path.join(path, file_name)
        if os.path.isfile(file_path) == False:
            try:
                response = requests.get(subtitle_url)
                with open(file_path, "wb") as f:
                    f.write(response.content)
            except:
                continue