import csv

from bs4 import BeautifulSoup
import requests

base_url = "http://everydayword.ru%s"
url = "http://everydayword.ru/glossary?page=%d"
url_list = []
for page_number in range(0, 55):
    url_list.append(url % page_number)

word_list = []
href_list = []

for url in url_list:
    #print(url)
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    data = soup.findAll('h2')
    for row in data:
        link = row.find('a')
        if link is not None:
            href = link['href']
            #print(href)
            #print(link.string)
            word_list.append(link.string)
            href_list.append(base_url % href)

word_dict = dict(zip(word_list, href_list))
print(word_dict)
w = csv.writer(open("output.csv", "w"))
for key, val in word_dict.items():
    #print(key,val)
    w.writerow([key, val])
