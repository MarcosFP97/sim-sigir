import pandas as pd
import ast
import os
from urllib.parse import urlparse

real_data = pd.read_csv('./data/filtered_data.csv')
overall_bias = pd.read_csv('./data/overall_bias.csv', sep=';')

total, found = 0, 0
for serp in real_data["ALL_URLS"].values:
    serp = ast.literal_eval(serp)
    for url in serp:
        domain = urlparse(url).netloc
        domain = domain.replace('www.', '')
        if domain in overall_bias["domain"].values:
            found+=1
        total+=1

print(f"Avg with newsguard in real data: {found/total}")

total, found = 0, 0
for f in os.listdir('./sim_output/title_snippet'):
  if f.startswith('session_title_snippet_steps'):
    df = pd.read_csv('./sim_output/title_snippet/'+f)
    for serp in df["SERP"].values:
        serp = ast.literal_eval(serp)
        for val in serp.values():
            url = val["URL"]
            domain = urlparse(url).netloc
            domain = domain.replace('www.', '')
            if domain in overall_bias["domain"].values:
                found+=1
            total+=1

print(f"Avg with newsguard in sim data: {found/total}")
