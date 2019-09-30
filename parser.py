#                       CREATED BY VARUN DAS                      #

import os
import requests
from bs4 import BeautifulSoup
import shutil

tags_needed = []
names_repo = []

extension_count = {
     'C++': 0,
     'C': 0,
     'PHP': 0,
     'HTML': 0,
     'CSS': 0,
     'Python': 0,
     'R': 0,
     'RUBY': 0,
     'KOTLIN': 0,
     'Javascript': 0,
     'RUST': 0,
     'GO': 0
}

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

def get_html1():
    fname = open('Parsed_Html1.txt', 'w')
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
    try:
        os.mkdir(repo)
    except:
        shutil.rmtree(repo)
        os.mkdir(repo)

    os.chdir(os.path.join(os.getcwd(), repo))
    for i in tags_needed:
        os.makedirs(i)

def is_extension(filename):
    extension = {'C++': '.cpp' ,
                 'C': '.c',
                 'PHP': '.php',
                 'HTML': '.html',
                 'CSS': '.css',
                 'Python': '.py',
                 'R': '.r',
                 'RUBY': '.rb',
                 'KOTLIN': '.kt',
                 'Javascript': '.js',
                 'RUST': '.rs',
                 'GO': '.go'
                 }

    for i in extension:
        if filename.endswith(extension[i]):
            extension_count[i] += 1
            break

def reset_extension_count():
    extension_count = {
         'C++': 0,
         'C': 0,
         'PHP': 0,
         'HTML': 0,
         'CSS': 0,
         'Python': 0,
         'R': 0,
         'RUBY': 0,
         'KOTLIN': 0,
         'Javascript': 0,
         'RUST': 0,
         'GO': 0
    }
    return extension_count

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
now = os.getcwd()
tags_needed = []

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


    print('Files in the repository: ')

    tag_extraction_for_repo()
    for i in tags_needed:
        print(i)
    print()

    os.chdir(now)

    create_initial_directories()

    dirs_web_new = []
    for i in tags_needed:
        dirs_web_new.append(url + '/blob/master/' + i)

    for dir in dirs_web_new:
        tags_needed = []
        html = requests.get(dir)
        soup = BeautifulSoup(html.text, 'html.parser')
        get_html1()
        tag_extraction_for_repo()


        for i in tags_needed:
            is_extension(i)
    for i in extension_count:
        s = ' ' * (10 - len(i))
        print(i,s,' : ',extension_count[i])
    extension_count = reset_extension_count()
    tags_needed = []
