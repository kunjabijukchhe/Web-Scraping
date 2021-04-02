from bs4 import BeautifulSoup
import requests
import time
print('Put some skill that you are familiar')
unfamiliar_skill=input('>')
print(f'filtering out {unfamiliar_skill}')

def find_job():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs =soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    for job in jobs:
        published_date=job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            company_name=job.find('h3',class_='joblist-comp-name').text.replace(' ', '')
            skill=job.find('span', class_='srp-skills').text.replace(' ', '')
            more_info=job.header.h2.a['href']
            if unfamiliar_skill not in skill:

            # print(published_date)
                print(f'Company Name: {company_name.strip()}')
                print(f'Required Skills: {skill.strip()}')
                print(f'More Info: {more_info}')

                print('')

if __name__ =='__main__':
    while True:
        find_job()
        time_wait=10
        print(f'Wating {time_wait} seconds...')
        time.sleep(time_wait)


