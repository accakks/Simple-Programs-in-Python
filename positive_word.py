import requests
from bs4 import BeautifulSoup

def get_random_word():
    page = requests.get('https://www.scrapmaker.com/view/sentiment/positive-words-all.txta')
    if page.status_code == 200:
        soup = BeautifulSoup(page.content, 'html.parser')
        try:
            word = str(soup.find_all('pre', class_='cols')[0]).split('<br/>')[2].title()
        
            return word
        except:
            return 'Not here'
    else:
        return 'Surprise'

if __name__ == "__main__":
    print(get_random_word())
