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

list_authors = {
    "First author": [],
    "Second author": [],
    "Last author": []
}

for i in range(52):
    source = requests.get("https://pubmed.ncbi.nlm.nih.gov/?term=anorexia%20nervosa&filter=simsearch1.fha&filter=hum_ani.animal&filter=lang.english&page=" + str(i)).text
    soup = BeautifulSoup(source, "lxml")
    
    for authors in soup.find_all("span", class_="docsum-authors full-authors"):
        authors = authors.text
        #authors = str(authors)
        authors = authors.split()
        #print(authors)
        ### To do: learn Pandas to append author information in a dataframe
        if len(authors) <= 3:
            first_author = authors[0] + " " + authors[1]
            list_authors["First author"].append(first_author[:-1])
            list_authors["Second author"].append("")
            list_authors["Last author"].append("")

        elif len(authors) <= 5:
            first_author = authors[0] + " " + authors[1]
            second_author = authors[2] + " " + authors[3]

            list_authors["First author"].append(first_author[:-1])
            list_authors["Second author"].append(second_author[:-1])
            list_authors["Last author"].append("")

        else:
            first_author = authors[0] + " " + authors[1]
            second_author = authors[2] + " " + authors[3]
            last_author = authors[-2] + " " + authors[-1]

            list_authors["First author"].append(first_author[:-1])
            list_authors["Second author"].append(second_author[:-1])
            list_authors["Last author"].append(last_author[:-1])

    print("Page " + str(i))
        
df = pd.DataFrame(list_authors)
print(df)
df.to_csv("author_test.csv", index=False)