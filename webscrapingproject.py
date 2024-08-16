from bs4 import BeautifulSoup
import requests

source = requests.get('https://web.archive.org/web/20171019235429/https://coreyms.com/').text #might not work properly due to being a web archive version of the site

soup = BeautifulSoup(source, 'lxml')

for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    vid_src = article.find('iframe', class_='youtube-player')['src']

    vid_id = vid_src.split('/')[9]
    vid_id = vid_id.split('?')[0]

    yt_link = f'https://youtube.com/watch/?v={vid_id}'
    print(yt_link)

    print()