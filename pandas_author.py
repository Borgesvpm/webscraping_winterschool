import pandas as pd
import re
import matplotlib.pyplot as plt

authorlist = [] 

df = pd.read_csv("pubmed_db2.csv")
authors = df['Authors']

for i in range(len(authors)):
    inside_list = authors[i]
    inside_list = inside_list.lower()
    inside_list = inside_list.split(", ")
    for j in range(len(inside_list)): 
        inside_list[j] = inside_list[j].replace("[", "")
        inside_list[j] = inside_list[j].replace("]", "")
        inside_list[j] = inside_list[j].replace("'", "")
        inside_list[j] = inside_list[j].replace('"', "")
        inside_list[j] = inside_list[j].replace(".", "")
    authorlist = authorlist + inside_list

db = pd.DataFrame(authorlist)
db.columns = ["Authors"]
db.Authors.value_counts()[:10].plot(kind='barh')
plt.show()

# frequency count
#df['count'] = df.groupby('group')['group'].transform('count')
#print(merged_df)
#db = pd.DataFrame(authorlist)
#print(db)
#db.value_counts(ascending=True)[30:].plot(kind='barh')
#plt.show()