from bs4 import BeautifulSoup
import requests
import time
import csv


def find_job():
    print('Search Your Interested filed(python,java...)')
    userInputURL = input('>')
    print(f'Searching your field {userInputURL}')
    with open(f'merojob/detail/{userInputURL}.csv', 'w', encoding="utf-8", newline='') as outcsv:
        writers=csv.writer(outcsv)
        writers.writerow(["Job Title","Company Name","Location","Required Skills","More Info"])

    for i in range(1,84):
        # addURL='https://merojob.com/search/?'+f'page={i}'
        addURL='https://merojob.com/search/?q='+userInputURL+f'&page={i}'
        print(addURL)
        html_text = requests.get(addURL).text
        soup = BeautifulSoup(html_text, 'lxml')
        links = soup.find_all('div',class_='col-lg-9 col-md-9 pl-0 pt-2')
        for link in links: 
            jobTitle = link.find('a',class_='no-uline').text

            if True:
                try:
                    companyName=link.find('a',class_='text-dark').text
                
                except AttributeError:
                    companyName ="NULL"
            if True:
                try:
                    location = link.find('span', itemprop="addressLocality").text
                except AttributeError:
                    location ="NULL"
            if True:
                try:    
                    skills = link.find('span', itemprop='skills').text.replace('\n',' ')
                except AttributeError:
                    skills  ="NULL"
            more_info=link.h1.a['href']
            with open(f'merojob/detail/{userInputURL}.csv','a', encoding="utf-8", newline='') as f:
                a = jobTitle.strip()
                b = companyName.strip()
                c = location.strip()
                d = skills.strip().replace(' ',', ')
                e = 'https://merojob.com'+more_info
                writers=csv.writer(f)
                writers.writerow([a,b,c,d,e])
               

if __name__ =='__main__':
    find_job()










