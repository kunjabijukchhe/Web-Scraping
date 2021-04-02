# from bs4 import BeautifulSoup

# with open('home.html', 'r') as html_file:
#     content = html_file.read()
#     # print(content)

#     soup = BeautifulSoup(content, 'lxml')
#     # # print(soup.prettify())

#     # # tags = soup.find('h1')
#     # # print(tags)
#     # courses_html_tages = soup.find_all('h1')
#     # # print(courses_html_tages)
#     # for course in courses_html_tages:
#     #     print(course.text)

#     course_cards = soup.find_all('div',class_='container')
#     for course in course_cards:
#         # print(course)
#         # print(course.h1)
#         course_name=course.h1.text
#         # course_link=course.a.text.split()[:-1]
#         course_link=course.a.text

#         # print(course_name)
#         # print(course_link)
#         print(f'{course_name} go to {course_link}')

# Real Website Scripting
from bs4 import BeautifulSoup
import requests

# html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=')
# print(html_text)
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
# print(html_text)

soup = BeautifulSoup(html_text, 'lxml')
jobs =soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
for job in jobs:
    published_date=job.find('span', class_='sim-posted').span.text
    if 'few' in published_date:
        company_name=job.find('h3',class_='joblist-comp-name').text.replace(' ', '')
        skill=job.find('span', class_='srp-skills').text.replace(' ', '')
        more_info=job.header.h2.a['href']
        # print(published_date)
        print(f'Company Name: {company_name.strip()}')
        print(f'Required Skills: {skill.strip()}')
        print(f'More Info: {more_info}')

        print('')








