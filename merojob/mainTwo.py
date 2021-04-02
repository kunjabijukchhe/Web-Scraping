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
        # writers.writerow(["Job Title","Company Name","Location","Required Skills","More Info"])
        writers.writerow(["Job Title","Company Name","More Info"])

    for i in range(1,5):
        addURL='https://merojob.com/search/?q='+userInputURL+f'&page={i}'
        print(addURL)
        html_text = requests.get(addURL).text
        # html_text = requests.get('https://merojob.com/search/?q=python&page=3').text
        soup = BeautifulSoup(html_text, 'lxml')
        links = soup.find_all('div',class_='col-lg-9 col-md-9 pl-0 pt-2')
        for link in links: 
            jobTitle = link.find('a',class_='no-uline').text
            companyName = link.find('a',class_='text-dark').text
            # location = link.find('span', itemprop="addressLocality").text
            # skills = link.find('span', itemprop='skills').text.replace('\n',' ')
            more_info=link.h1.a['href']
            with open(f'merojob/detail/{userInputURL}.csv','a', newline='') as f:
                a=jobTitle.strip()
                b=companyName.strip()
                # c=location.strip()
                # d=skills.strip().replace(' ',', ')
                e='https://merojob.com'+more_info
                writers=csv.writer(f)
                # writers.writerow([a,b,c,d,e])
                writers.writerow([a,b,e])

if __name__ =='__main__':
    find_job()










