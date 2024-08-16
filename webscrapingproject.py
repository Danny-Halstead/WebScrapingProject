from bs4 import BeautifulSoup
import requests

source = requests

with open('Simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

