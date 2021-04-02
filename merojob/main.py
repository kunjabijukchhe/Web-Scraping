from bs4 import BeautifulSoup
import requests
import time
import csv
print('Input url from search job like: https://merojob.com/search/?q=python')
userInputURL=input('>')


print(f'searching {userInputURL}')

html_text = requests.get(userInputURL).text
soup = BeautifulSoup(html_text, 'lxml')
links = soup.find_all('div',class_='col-lg-9 col-md-9 pl-0 pt-2')
for index,link in enumerate(links): 
    jobTitle = link.find('a',class_='no-uline').text
    companyName = link.find('a',class_='text-dark').text
    location = link.find('span', itemprop="addressLocality").text
    skills = link.find('span', itemprop='skills').text.replace('\n',' ')
    more_info=link.h1.a['href']
    with open(f'merojob/detail/file.csv','a') as f:
        f.write(f'Job Title: {jobTitle.strip()}\n')
        f.write(f'Company Name: {companyName.strip()}\n')
        f.write(f'Location: {location.strip()}\n')
        if not skills:
            f.write("NULL")           
        else:
            f.write(f'Required Skills: {skills.strip()}\n')
        f.write(f'More Info: https://merojob.com{more_info}\n')
        f.write('\n\n')
    









