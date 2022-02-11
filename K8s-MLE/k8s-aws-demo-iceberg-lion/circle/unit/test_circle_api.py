#pylint: disable=missing-final-newline,missing-module-docstring,import-error,c0325,c0303,c0301,c0115,c0116,w1401,c0413,w0622,r1705,r1716,w0622,w0611,c0411,e1120,r1710,r0903,c0103,e0402
import sys
import pytest
import requests
from bs4 import BeautifulSoup
sys.path.insert(0,"..")
import circle
import scraper

def test_circle_valid_params():
    url = ""
    myC = circle.Circle(float(1)).perimeter()
    apiC = scraper.Scraper(str(url)).scrape_site()
    assert round(myC.area(),2) == apiC
    # assert round(myC.perimeter(),2) == 6.28    
    assert myC.summary() == 'area=3.14, perimeter=6.28'
