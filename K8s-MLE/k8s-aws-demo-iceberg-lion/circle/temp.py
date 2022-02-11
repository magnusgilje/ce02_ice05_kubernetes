#pylint: disable=missing-final-newline,missing-module-docstring,import-error,c0325,c0303,c0301,c0115,c0116,w1401,c0413,w0622,r1705,r1716,w0622,w0611,c0411,e1120,r1710,r0903,c0103
import scraper

def scrape():
    url="http://127.0.0.1:8000/"
    apiC = scraper.Scraper(str(url)).scrape_site()
    print(apiC)
