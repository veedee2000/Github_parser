#                       CREATED BY VARUN DAS                      #

import os
import requests
from bs4 import BeautifulSoup
import shutil

tags_needed = []
names_repo = []

def tag_extraction_for_all():
    tags_crude = soup.findAll('h3')

    for tag in tags_crude:
        anchor_tags = tag('a')

        for i in anchor_tags:
            text_needed = i.get('href')
            names_repo.append(i.get_text().strip())
            tags_needed.append(base_url[0:len(base_url) - 1] + text_needed)


def get_html():
    fname = open('Parsed_Html.txt', 'w')
    fname.write(soup.prettify())
    fname.close()

def say_bye():
    fname = open('Parsed_Html.txt', 'w')
    fname.write('BYE-BYE  :)')
    fname.close()

def tag_extraction_for_repo():
    tags_crudes = soup('td',{'class':'content'})
    for tags_crude in tags_crudes:
        if tags_crude.get_text().strip() != 'Failed to load latest commit information.':
            tags_needed.append(tags_crude.get_text().strip())

def create_initial_directories():
    for i in tags_needed:
        shutil.rmtree(i)
        os.makedirs(i)

def get_extension():
    if


def fill_dir():
    for i in tags_needed:
        os.chdir(os.getcwd() + '/'.format(i))




### --------------------------MAIN -----------------------------###

base_url = 'http://github.com/'

print('Ready - Set - GO ')
print()

username = input('Enter username: ')
print()

url = base_url + username + '?tab=repositories'
html = requests.get(url)

soup = BeautifulSoup(html.text, 'html.parser')

get_html()
tag_extraction_for_all()

print('There are {} repositories in the github account of {}'.format(len(tags_needed), username))
print()

for i in names_repo:
    print(i)
print()

while 1:

    val = input('Press 0 to exit or any other digit to continue: ')
    if int(val) == 0:
        say_bye()
        quit()
    print()
    repo = input('Enter the repository name you would like to parse: ');
    print()
    print('Parsing repo : ',repo)

    url = base_url + username + '/' + repo
    print('url : ',url)
    print()
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    get_html()

    tags_needed = []
    tag_extraction_for_repo()

    print('Files in the repository: ')

    for i in tags_needed:
        print(i)
    print()

    create_initial_directories()

    fill_dir()
