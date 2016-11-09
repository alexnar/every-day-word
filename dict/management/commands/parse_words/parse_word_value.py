import csv
from bs4 import BeautifulSoup
import requests


def parse_words():
    word_dict = {}
    url_list = []
    for key, val in csv.reader(open("output.csv", "r")):
        word_dict[key] = val

    for key in word_dict:
        url = word_dict[key]
        print(url)
        r = requests.get(url)
        data = r.text
        soup = BeautifulSoup(data, 'html.parser')
        definition = soup.findAll(attrs={'class': 'definition'})[0]
        definition = definition.find('div').find('div').find('div')
        word_dict[key] = definition.string
        # print(word_dict[key])

    w = csv.writer(open("dict.csv", "w"))
    for key, val in word_dict.items():
        # print([key, val])
        w.writerow([key, val])


def main():
    pass


if __name__ == "__main__":
    main()
