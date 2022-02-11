#pylint: disable=missing-final-newline,missing-module-docstring,import-error,c0325,c0303,c0301,c0115,c0116,w1401,c0413,w0622,r1705,r1716,w0622,w0611,c0411,e1120,r1710,r0903
import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self,url:str):
        self.url = url

    def scrape_site(self):
        page = requests.get(self.url)
        if page.status_code == 200:
            soup = BeautifulSoup(page.content, 'html.parser')
            for script_or_style in soup(["script", "style"]):
                script_or_style.extract()
            text = soup.get_text()
            # return {' '.join(text.split())}
            return text
    if __name__ == "__main__":
        scrape_site()
