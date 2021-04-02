from bs4 import BeautifulSoup
import requests
import time

html_text = requests.get('https://www.instagram.com/malla.surakshya/').text
soup = BeautifulSoup(html_text, 'lxml')
links = soup.find_all('div',class_='_2z6nI')
# print(links)
for link in links: 
    
    image = link.find('img',class_='FFVAD').text
    print(image)