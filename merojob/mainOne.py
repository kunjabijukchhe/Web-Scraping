from bs4 import BeautifulSoup
import requests
import time
import csv


def find_job():
    print('Search Your Interested filed(python,java...)')
    userInputURL=input('>')
    print(f'Searching your field {userInputURL}')
    with open(f'merojob/detail/{userInputURL}.csv', 'w', newline='') as outcsv:
        writers=csv.writer(outcsv)
        writers.writerow(["Job Title","Company Name","Location","Required Skills","Post Date and Time","More Info"])

    for i in range(1,84):
        addURL='https://merojob.com/search/?'+f'page={i}'
        # addURL='https://merojob.com/search/?q='+userInputURL+f'&page={i}'
        print(addURL)
        html_text = requests.get(addURL).text

        soup = BeautifulSoup(html_text, 'lxml')
        links = soup.find_all('div',class_='card mt-3 hover-shadow')
        for link in links: 
            jobTitle = link.find('a',class_='no-uline').text
            # jobTitle = link.a['title']
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
            if True:
                try:    
                    postdate = link.p.meta['content']
                except AttributeError:
                    postdate= "NULL"
            more_info=link.h1.a['href']
            with open(f'merojob/detail/{userInputURL}.csv','a', newline='', encoding="utf-8") as f:
                a=jobTitle.strip()
                b=companyName.strip()
                c=location.strip()
                d=skills.strip().replace(' ',', ')
                pd=postdate.strip()
                e='https://merojob.com'+more_info
                writers=csv.writer(f)
                writers.writerow([a,b,c,d,pd,e])
         

if __name__ =='__main__':
    find_job()










