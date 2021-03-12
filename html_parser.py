
import requests
from bs4 import BeautifulSoup


class Parser:
    def __init__(self, url, headers):
        self.url = url,
        self.headers = headers

    def get_html(self, url):
        try:
            return requests.get(url, headers=self.headers)
        except requests.exceptions.MissingSchema:
            print("Incorrect address.")
            return None

    @staticmethod
    def get_content(html):
        soup = BeautifulSoup(html, 'html.parser')
        return soup.text

    def parse(self):
        html = self.get_html(self.url[0])
        try:
            if html.status_code == 200:
                return self.get_content(html.text)
        except AttributeError:
            return ''
