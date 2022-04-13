import requests
import re


def download_subtitle(url,name):
    """
    downloads subtitle
    """

    page = requests.get(url).text

    file = re.findall("https.*.zip",page)
    if file == []:
        file = re.findall("https.*.rar",page)

    d_file = requests.get(file[0])

    open(name + '.zip', 'wb').write(d_file.content)


