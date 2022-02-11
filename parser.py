from bs4 import BeautifulSoup
from urllib.request import urlopen


url = [
    "https://habr.com/ru/company/renins/blog/564522/",
    "https://habr.com/ru/company/2gis/blog/649175/"
]


file = open('text_pars.txt', 'a')


for x in url:
    html_code = str(urlopen(x).read(), 'utf-8')
    soup = BeautifulSoup(html_code, 'html.parser')

    s = soup.find('title').text
    file.write(s + '\n')
    p = soup.find_all('p')
    print(s)
    for i in p:
        print(i.text)
        file.write(i.text + '\n\n')

file.close()
