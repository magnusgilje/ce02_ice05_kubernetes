#pylint: disable=c0305,c0301,c0116,c0103,c0303,w0511,r0914,w0613,w0612,r1705,w0703,c0114,c0325,c0410,c0413,e0401,c0411,w0611,e0102,r1721,c0121,w0621,w0622,e0012
from enum import Enum
from fastapi import FastAPI
import re
import os
import sys
sys.path.insert(0,"./")
import edgar_downloader, edgar_cleaner
import joblib
import ref_data as edgar_refdata
import text_preprocessor
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

df_sp100 = edgar_refdata.get_sp100()
tickers_dict  = df_sp100['Symbol']
input_folder = r'C:\temp\junk\10k_reports_raw'

app=FastAPI()

@app.get("/")
async def root():
    return {"message": "Edgar api"}

@app.get("/html/{ticker}/{year}")
async def root(ticker: str, year:str):
    tickers_list=[]
    for i in tickers_dict:
        tickers_list.append(i)

    if (ticker not in tickers_list):
        return{"Error": "ticker not recognised"}

    if int(year)> 2021 or int(year)<2000:
        return {"ERROR":"invalid year"}
    fileName = "file not found"
    html_files = [f for f in os.listdir(input_folder)]
    in_file_path = False
    for i in html_files:
        if ticker in i and year in i:
            in_file_path = True
            fileName = i
    if in_file_path == False:
        edgar_downloader.download_files_10k(ticker, input_folder, year)
        html_files = [f for f in os.listdir(input_folder)]
        print('------------------------------')
        for i in html_files:
            if ticker in i and year in i:
                in_file_path = True
                fileName = i
    
    localUrl = fr'C:\temp\junk\10k_reports_raw\{fileName}'
    with open(localUrl, 'r') as file:
        fileContents = file.read()
    
    return{"message": fileContents}
    


@app.get("/sentiment/{ticker}/{year}")
async def root(ticker: str, year: str):
    for f in os.listdir('downloads'):
        os.remove(os.path.join('downloads', f))
    for f in os.listdir('downloads_cleaned'):
        os.remove(os.path.join('downloads_cleaned', f))
     # Get clean 10-k filing
    edgar_downloader.download_files_10k(ticker,'downloads',year)

    dir='downloads'

    for root, dirs, files in os.walk(dir):
        for name in files:
            if year not in name:
                os.remove(os.path.join(root, name))

    edgar_cleaner.write_clean_html_text_files('downloads','downloads_cleaned')

    for root, dirs, files in os.walk('downloads_cleaned'):
        for name in files:
            text = text_preprocessor.process_text_files(os.path.join(root,name))
    #return text
        
    #Load in model
    vectorizer = joblib.load('Tfidfvectorizer.joblib')
    text = vectorizer.transform([text])

    model = joblib.load('model.joblib')
    movement_proba = model.predict_proba(text)

    if movement_proba[0][1]<0.25:
        recommendation = 'SELL'

    elif movement_proba[0][1]>0.75:
        recommendation = 'BUY'

    else:
        recommendation = 'HOLD'
    
    return{f'{ticker},{year}': 
        {"P(stonk goes up)":movement_proba[0][1],
        "P(stonk goes down)":1-movement_proba[0][1],
        "recommendation":recommendation
        }
    }
    

@app.get("/txt/{ticker}/{year}")
async def root(ticker: str, year: str):
    return{ticker: "text file" + " " + year}
