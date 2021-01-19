# Research how to properly document code

"""Webscrappes author information from all pages of a PubMed page.

    Retrives author information from the webpage xml structure, generates two .csv files:
    - One with all author information (first, second, last)
    - One with the author count

"""

from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd
import numpy as np
import csv
import time

db_list = {
    "Authors": [],
    "Title": [],
    "Journal" : [],
    "Abstract": [],
    "Keywords": []
}

for i in range(51):
    source = requests.get("https://pubmed.ncbi.nlm.nih.gov/?term=anorexia%20nervosa&filter=simsearch1.fha&filter=hum_ani.animal&filter=lang.english&page=" + str(i)).text
    soup = BeautifulSoup(source, "lxml")
    
    for authors in soup.find_all("span", class_="docsum-authors full-authors"):
        authors = authors.text
        authors = authors.split(", ")
        db_list["Authors"].append(authors)

    for titles in soup.find_all("a", class_="docsum-title"):
        titles = titles.text
        titles = titles.strip()
        db_list["Title"].append(titles)
    
    for journals in soup.find_all("span", class_="docsum-journal-citation short-journal-citation"):
        journals = journals.text
        journals = journals.split(". ")
        journals = journals[0]
        db_list["Journal"].append(journals)

    # getting abstracts requires moving inside the actual paper page
    for pmid in soup.find_all("span", class_="docsum-pmid"):
        pmid = pmid.text

        source_abs = requests.get("https://pubmed.ncbi.nlm.nih.gov/" + pmid)
        source_abs = source_abs.text
        soup_abs = BeautifulSoup(source_abs, "lxml")

        abstracts = soup_abs.find("div", class_="abstract-content selected")
        abstracts = abstracts.text
        abstracts = abstracts.strip() 
        db_list["Abstract"].append(abstracts)

        try:
            keywords =  soup_abs.find("div", class_="abstract").findAll('p')
            keywords = str(keywords)
            keywords = keywords.split("Keywords",1)[1]
            keywords = keywords.split("\n")[3]
            keywords = keywords.strip()
            print(keywords)
            keywords = keywords.replace('.','')
            keywords = keywords.lower()
            db_list["Keywords"].append(keywords)
        except:
            db_list["Keywords"].append("\t")

    print(db_list)
    time.sleep(1)

print("Page " + str(i+1))
        
df = pd.DataFrame(db_list)
print(df)
df.to_csv("pubmed_db2.csv", encoding='utf-8-sig', index=False)