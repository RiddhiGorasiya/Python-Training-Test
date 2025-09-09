import requests
from bs4 import BeautifulSoup

def extract_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for a_tag in soup.find_all('a'):
        href = a_tag.get('href')
        if href:
            yield href  
            
url = 'https://www.python.org'
for link in extract_links(url):
    print(link)
