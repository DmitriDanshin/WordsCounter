from html_parser import Parser
from counter import Counter
from database import DataBase


URL = "https://www.google.com/"
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 '
                  'Safari/537.36',
    'accept': '*/*'
}
DIVS = " ,:@.-()/!?"

if __name__ == '__main__':
    URL = input("Type your URL: ")
    html_text = Parser(url=URL, headers=HEADERS).parse()
    c = Counter(html_text, divider=DIVS).count_words()
    db = DataBase()
    db.make_database(c)
    print(c)
