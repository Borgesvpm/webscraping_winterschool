import pandas as pd
import re
import matplotlib.pyplot as plt
import time

df = pd.read_csv("pubmed_db2.csv")
df["Interest"] = 0

for i in range(len(df['Keywords'])):
    if df['Keywords'][i].find("photometry") != -1:
        df["Interest"][i] = df["Interest"][i] + 10

    if df['Keywords'][i].find("miniscope") != -1:
        df["Interest"][i] = df["Interest"][i] + 20

    if df['Keywords'][i].find("hypothalam") != -1:
        df["Interest"][i] = df["Interest"][i] + 5

df.sort_values(["Interest"], inplace=True)
df.to_csv("pubmed_db2_interest.csv", encoding='utf-8-sig', index=False)
