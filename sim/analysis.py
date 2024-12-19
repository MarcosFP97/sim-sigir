import pandas as pd
import ast
import os
from urllib.parse import urlparse
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re
from wordfreq import word_frequency

######### PERCENTAGE OF ENTRIES WITH NEWS GUARD SCORE

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


##### QUERY LENGTH ANALYSIS

dfs = []
for f in os.listdir('./sim_output/paragraph_full_text/bing-api/'):
  if f.startswith('session_paragraph_full_text_steps'):
    df = pd.read_csv('./sim_output/paragraph_full_text/bing-api/'+f)
    df = df[['query', 'AVG_SCORE']]
    df["query_length"] = df['query'].apply(lambda x: len(word_tokenize(str(x))))
    dfs.append(df)

df = pd.concat(dfs)
print(df.head())
df = df.dropna()
print(len(df))
df.sort_values('AVG_SCORE', inplace=True)
print(f'Average length of the best queries {np.mean(df.iloc[:100,:]["query_length"])}')
print(f'Average length of the worst queries {np.mean(df.iloc[-100:,:]["query_length"])}')


##### TECHNICAL TERMS ANALYSIS

def preprocess_queries(queries):
    stop_words = set(stopwords.words("english"))
    cleaned_queries = []
    for query in queries:
        # Quitar puntuación y convertir a minúsculas
        cleaned_query = re.sub(r'[^\w\s]', '', query.lower())
        # Eliminar stopwords
        cleaned_query = ' '.join([word for word in cleaned_query.split() if word not in stop_words])
        cleaned_queries.append(cleaned_query)
    return cleaned_queries

best_queries = df.iloc[:100,:]["query"].values
worst_queries = df.iloc[-100:,:]["query"].values



best_queries_cleaned = preprocess_queries(best_queries)
worst_queries_cleaned = preprocess_queries(worst_queries)

count, less = 0,0
for query in best_queries_cleaned:
    terms = word_tokenize(query)
    for term in terms:
        freq = word_frequency(term, 'en')
        if freq < 1e-6:  # Threshold para términos raros
            less+=1 # si la query contiene al menos un término poco frecuente
        break
    count+=1
print(f'Technical terms in good queries {less/count}')

count, less = 0,0
for query in worst_queries_cleaned:
    terms = word_tokenize(query)
    for term in terms:
        freq = word_frequency(term, 'en')
        if freq < 1e-6:  # Threshold para términos raros
            less+=1 # si la query contiene al menos un término poco frecuente
        break
    count+=1
print(f'Technical terms in bad queries {less/count}')

dfs_2 = []
for f in os.listdir('./sim_output/title_snippet/bing-api/'):
  if f.startswith('session_title_snippet_steps'):
    df = pd.read_csv('./sim_output/title_snippet/bing-api/'+f)
    df = df[['query', 'AVG_SCORE']]
    df["query_length"] = df['query'].apply(lambda x: len(word_tokenize(str(x))))
    dfs_2.append(df)

second = pd.concat(dfs_2)
second = second.dropna()

best_variant_queries_cleaned = preprocess_queries(df.iloc[:100,:]["query"].values)
worst_variant_queries_cleaned = preprocess_queries(second.iloc[:100,:]["query"].values)

count, less = 0,0
for query in best_variant_queries_cleaned:
    terms = word_tokenize(query)
    for term in terms:
        freq = word_frequency(term, 'en')
        if freq < 1e-6:  # Threshold para términos raros
            less+=1 # si la query contiene al menos un término poco frecuente
        break
    count+=1
print(f'Technical terms in best variant {less/count}')

count, less = 0,0
for query in worst_variant_queries_cleaned:
    terms = word_tokenize(query)
    for term in terms:
        freq = word_frequency(term, 'en')
        if freq < 1e-6:  # Threshold para términos raros
            less+=1 # si la query contiene al menos un término poco frecuente
        break
    count+=1
print(f'Technical terms in worst variant {less/count}')