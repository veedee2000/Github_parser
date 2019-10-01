#                       CREATED BY VARUN DAS                      #

import os
import re
import plotly.graph_objects as go
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


def tag_extraction_for_repo_sec(initial):
    tags_crudes = soup('td',{'class':'content'})
    for tags_crude in tags_crudes:
        if tags_crude.get_text().strip() != 'Failed to load latest commit information.':
            tags_needed_sec.append(initial + '/' + tags_crude.get_text().strip())


def check_if_file(filename):
    for i in filename:
        if i == '.':
            is_extension(filename)
            return True
    return False


def create_initial_directory(repo):
    try:
        os.mkdir(repo)
    except:
        shutil.rmtree(repo)
        os.mkdir(repo)


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


def extract_file_name(i):
    s = re.findall('/([a-zA-Z0-9\._-]+)$', i)
    return s[0]


def write_in_file(dir, file_name):
    html = requests.get(url + '/blob/master/' + dir)
    soup = BeautifulSoup(html.text, 'html.parser')
    val = soup('td', {'class':'blob-code blob-code-inner js-file-line'})
    fname = open(file_name, 'w')

    for i in val:
        fname.write(i.get_text() + '\n')
    fname.close()

def plot_with_plotly():
    labels = []
    values = []
    for i in extension_count:
        labels.append(i)
        values.append(extension_count[i])
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig.show()

### --------------------------MAIN------------------------------###

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
    print()
    if int(val) == 0:
        say_bye()
        quit()

    repo = input('Enter the repository name you would like to parse: ');
    print()
    print('Parsing repo : ',repo)

    url = base_url + username + '/' + repo
    print('url : ',url)
    print()

    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    get_html()

    print('Repositories/Files in the Parent Repository: ')

    tag_extraction_for_repo()

    for i in tags_needed:
        print(i)
    print()

    os.chdir(now)

    tags_needed_sec = []

    while 1:
        filenames = []
        for dir in tags_needed:
            html = requests.get(url + '/blob/master/' + dir)
            soup = BeautifulSoup(html.text, 'html.parser')
            tag_extraction_for_repo_sec(dir)
        tags_needed = []
        for i in tags_needed_sec:
            if check_if_file(i) == False:
                tags_needed.append(i)
            else:
                filenames.append(i)
            tags_needed_sec = []
        if len(tags_needed) == 0: break

    create_initial_directory(repo)
    os.chdir(os.path.join(os.getcwd(), repo))

    for file in filenames:
        os.makedirs(file)

    get_repo_directory = os.getcwd()

    for i in filenames:
        os.chdir(os.path.join(get_repo_directory, i))
        file_name = extract_file_name(i)
        write_in_file(i, file_name)
    print('Total {} files parsed'.format(len(filenames)))
    print()

    print('Language       Number of programs')
    print()

    for i in extension_count:
        s = ' ' * (10 - len(i))
        if extension_count[i] > 0:
            print(i,s,' : ',extension_count[i])
    print()

    plot_with_plotly()
    extension_count = reset_extension_count()
