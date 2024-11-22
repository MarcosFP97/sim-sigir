import pandas as pd
from openai import OpenAI
import os
import json
import sys
import os
from pprint import pprint
import requests
import newspaper
import pandas as pd
from urllib.parse import urlparse
import numpy as np
import time
import numpy as np
import pandas as pd
from config import OPENAI_API_KEY, MODEL, BING_API_KEYS

def first_step_gen(
    headline:str,
    text:str
  ):
  if first_step_mode=="title":
    prompt= f'Given the headline of a webpage, generate a query that a user of a web retrieval engine would type to verify the correctness of the information provided in the webpage. \
        Avoid using stopwords. Queries should have between 3-5 words length.  Headline of the Webpage: {headline}\n Query:"' #### I added stopwords and correct information
  elif first_step_mode=="paragraph":
    prompt= f'Given the headline of a webpage and its first paragraph, generate a query that a user of a web retrieval engine would type to verify the correctness of the information provided in the webpage. \
        Avoid using stopwords. Queries should have between 3-5 words length.  Headline of the Webpage: {headline}\n First Paragraph of the Webpage:{text}\n Query:"' #### I added stopwords and correct information
  elif first_step_mode=="full_text":
    prompt= f'Given the headline of a webpage and its body, generate a query that a user of a web retrieval engine would type to verify the correctness of the information provided in the webpage. \
        Avoid using stopwords. Queries should have between 3-5 words length.  Headline of the Webpage: {headline}\n Body of the Webpage:{text}\n Query:"' #### I added stopwords and correct information
  completion = client.chat.completions.create(
    model=MODEL,
    messages=[
      {"role": "system", "content": "You are a search query writer"},
      {"role": "user", "content": prompt}
    ],
    temperature=0.7
  )

  return completion.choices[0].message.content

def second_step_gen(
    headline:str,
    text:str, # either first paragrph or full text
    old_queries:list,
    snippets_concated:str,
    full_text_snippets:str
  ):
  if second_step_mode=="snippet":
    if first_step_mode=="title":
      prompt= f'Given the headline of a webpage, a user has conducted a search session to verify the correctness of the information provided in the webpage.\
        We provide you with the user session queries and the results for the last search. For each search result, we provide you with its title and snippet.\
        Taking into account the headline of the webpage, the user session queries and the search results, your task is to generate a new user query \
        to further verify the correctness of the information provided in the webpage. \
        Avoid repeating the exact same queries and introduce some variance in the new query, but avoiding topic drift. \
        Avoid using stopwords. Queries should have between 3-5 words length. \
        Headline of the Webpage: {headline}\n \
        User Queries: \"{old_queries}\"\n \
        Search results: {snippets_concated}\nNew User Query:' #### I added stopwords and correct information
      print(prompt)
    ########## MODIFY PROMPTS!!!!
    elif first_step_mode=="paragraph":
      prompt= f'Given the headline of a webpage and its first paragraph, a user has typed a web query to verify the correctness of the information provided in the webpage.\
        We provide you with the user web query and its search results. For each search result, we provide you with its title and snippet.\
        Taking into account the headline of the webpage, its first paragraph, the user query and the search results, your task is to generate a new user query \
        to further verify the correctness of the information provided in the webpage. \
        Avoid using stopwords. Queries should have between 3-5 words length. \
        Headline of the Webpage: {headline}\n \
        First Paragraph of the Webpage: {text}\n \
        User Query: \"{old_queries}\" \n \
        Search results: {snippets_concated}\nNew User Query:' #### I added stopwords and correct information
    elif first_step_mode=="full_text":
      prompt= f'Given the headline of a webpage and its body, a user has typed a web query to verify the correctness of the information provided in the webpage.\
        We provide you with the user web query and its search results. For each search result, we provide you with its title and snippet.\
        Taking into account the headline of the webpage, its body, the user query and the search results, your task is to generate a new user query \
        to further verify the correctness of the information provided in the webpage. \
        Avoid using stopwords. Queries should have between 3-5 words length. \
        Headline of the Webpage: {headline}\n \
        Body of the Webpage: {text}\n \
        User Query: \"{old_queries}\" \n \
        Search results: {snippets_concated}\nNew User Query:' #### I added stopwords and correct information
    #print(prompt)
  elif second_step_mode=="full_text":
    if first_step_mode=="title":
      prompt= f'Given the headline of a webpage, a user has typed a web query to verify the correctness of the information provided in the webpage.\
          We provide you with the user web query and its search results. For each search result, we provide you with its title and snippet.\
          For the first two search results, we also provide you the entire document when available. \
          Taking into account the headline of the webpage, the user query and the search results, your task is to generate a new user query \
          to further verify the correctness of the information provided in the webpage. \
          Avoid using stopwords. Queries should have between 3-5 words length. \
          Headline of the Webpage: {headline}\n \
          User Query: \"{old_queries}\" \n \
          Search results: {full_text_snippets}\nNew User Query:' #### I added stopwords and correct information
    elif first_step_mode=="paragraph":
      prompt= f'Given the headline of a webpage and its first paragraph, a user has typed a web query to verify the correctness of the information provided in the webpage.\
          We provide you with the user web query and its search results. For each search result, we provide you with its title and snippet.\
          For the first two search results, we also provide you the entire document when available. \
          Taking into account the headline of the webpage, its first paragraph, the user query and the search results, your task is to generate a new user query \
          to further verify the correctness of the information provided in the webpage. \
          Avoid using stopwords. Queries should have between 3-5 words length. \
          Headline of the Webpage: {headline}\n \
          First Paragraph of the Webpage: {text}\n \
          User Query: \"{old_queries}\" \n \
          Search results: {full_text_snippets}\nNew User Query:' #### I added stopwords and correct information
    elif first_step_mode=="full_text":
      prompt= f'Given the headline of a webpage and its body, a user has typed a web query to verify the correctness of the information provided in the webpage.\
          We provide you with the user web query and its search results. For each search result, we provide you with its title and snippet.\
          For the first two search results, we also provide you the entire document when available. \
          Taking into account the headline of the webpage, its body, the user query and the search results, your task is to generate a new user query \
          to further verify the correctness of the information provided in the webpage. \
          Avoid using stopwords. Queries should have between 3-5 words length. \
          Headline of the Webpage: {headline}\n \
          Body of the Webpage: {text}\n \
          User Query: \"{old_queries}\" \n \
          Search results: {full_text_snippets}\nNew User Query:' #### I added stopwords and correct information

  completion = client.chat.completions.create(
    model=MODEL,
    messages=[
      {"role": "system", "content": "You are a search query writer"},
      {"role": "user", "content": prompt}
    ],
    temperature=0.7
  )

  return completion.choices[0].message.content

'''
This sample makes a call to the Bing Web Search API with a query and returns relevant web search.
Documentation: https://docs.microsoft.com/en-us/bing/search-apis/bing-web-search/overview
'''

def bing_search(
    query:str,
):
  # Add your Bing Search V7 subscription key and endpoint to your environment variables.
  keys = BING_API_KEYS
  endpoint = 'https://api.bing.microsoft.com/v7.0/search'

  # Construct a request
  mkt = 'en-US'
  params = { 'q': query, 'mkt': mkt, 'freshness': '2021-12-20..2023-12-20'}


  for key in keys:# Call the API
    print(f'Using key...{key}')
    headers = { 'Ocp-Apim-Subscription-Key': key }
    try:
        response = requests.get(endpoint, headers=headers, params=params)
        response.raise_for_status()
        res = response.json()

        serp = {}
        for i,val in enumerate(res["webPages"]["value"]):
          try: #### SI NO PUEDO RECUPERAR
            full_text = newspaper.article(val["url"])
            full_text  = full_text.text
          except:
            full_text = ""
          serp[i+1] = {'URL':val["url"], 'Headline':val["name"], 'Snippet':val["snippet"], 'Full_text':full_text}
        return serp
    except Exception as ex:
        continue

def eval_serp(serp):
  scores = pd.read_csv(DATA_DIR+'/overall_bias.csv', sep=';')

  newsguard = []
  for entry in serp.values():
    domain = urlparse(entry["URL"]).netloc
    domain = domain.replace('www.', '')
    if domain in scores["domain"].values:
      score = scores.loc[scores["domain"]==domain, "newsguard"].values[0]
      score = float(score.replace(',', '.'))
      newsguard.append(score)
  return np.mean(newsguard)

def simulate(corpus):
    ll = list({1,2,3,4,5,6,8})*5
    count=1 ######### THIS!!!
    for sample in ll: # samples: ##### THIS!!!
        print("=======SESSION STARTED=========")
        print(f"Session length: {sample}")
        cols = ["URL", "query", "SERP", "AVG_SCORE", "STEP"]
        session = pd.DataFrame(columns=cols)

        last_serps = {} ### variable para ir almacenando el último serp de cada artículo original
        session_queries = {}
        for i in range(sample):
            if i==0: ### the first step is always different
                print(f"STEP {i+1}")
                if first_step_mode=="title":
                    for orig_url, headline in zip(corpus["URL"].values, corpus["Headline"].values):
                    #### CALL TO GEN
                        query_gen = first_step_gen(headline, "")
                        query_gen = query_gen.replace('"', '')
                        if orig_url not in session_queries:
                           session_queries[orig_url] = []
                        session_queries[orig_url].append(query_gen)
                        print(session_queries[orig_url])
                        serp = bing_search(query_gen) ##### !!!!! I NEED TO MODIFY THE FRESHNESS
                        last_serps[orig_url] = [session_queries[orig_url], headline, "", serp] ### KEEPING TRACK OF THE LAST SERPS
                        time.sleep(2) ### DELAY IN CALLS TO BING SEARCH API
                        avg_score = eval_serp(serp)
                        print(avg_score)
                        newline = {"URL":orig_url, "query":query_gen, "SERP":serp, "AVG_SCORE": avg_score, "STEP": i+1}
                        session = pd.concat([session, pd.DataFrame([newline])], ignore_index=True)

                elif first_step_mode=="paragraph":
                    #### FUNCIÓN QUE CONCATENE TITLE Y FIRST PARAGRAPH
                    for orig_url, headline, text in zip(corpus["URL"].values, corpus["Headline"].values, corpus["plain_text"]):
                        #### CALL TO GEN
                        first_paragraph = text.split('\n')[0]
                        query_gen = first_step_gen(headline, first_paragraph)
                        query_gen = query_gen.replace('"', '')
                        print(query_gen)
                        serp = bing_search(query_gen) ##### !!!!! I NEED TO MODIFY THE FRESHNESS
                        last_serps[orig_url] = [query_gen, headline, text, serp] ### KEEPING TRACK OF THE LAST SERPS
                        time.sleep(2) ### DELAY IN CALLS TO BING SEARCH API
                        avg_score = eval_serp(serp)
                        newline = {"URL":orig_url, "query":query_gen, "SERP":serp, "AVG_SCORE": avg_score, "STEP": i+1}
                        session = pd.concat([session, pd.DataFrame([newline])], ignore_index=True)
                elif first_step_mode=="full_text":
                    #### FUNCIÓN QUE CONCATENE TITLE Y FULL TEXT
                    for orig_url, headline, text in zip(corpus["URL"].values, corpus["Headline"].values, corpus["plain_text"]):
                        #### CALL TO GEN
                        query_gen = first_step_gen(headline, text)
                        query_gen = query_gen.replace('"', '')
                        print(query_gen)
                        serp = bing_search(query_gen) ##### !!!!! I NEED TO MODIFY THE FRESHNESS
                        last_serps[orig_url] = [query_gen, headline, text, serp] ### KEEPING TRACK OF THE LAST SERPS
                        time.sleep(2) ### DELAY IN CALLS TO BING SEARCH API
                        avg_score = eval_serp(serp)
                        print(avg_score)
                        newline = {"URL":orig_url, "query":query_gen, "SERP":serp, "AVG_SCORE": avg_score, "STEP": i+1}
                        session = pd.concat([session, pd.DataFrame([newline])], ignore_index=True)
            else:
                #### SUBSEQUENT STEPS
                print(f"STEP {i+1}")
                if second_step_mode=='snippet':
                    for orig_url, serp in last_serps.items(): # WE USE THE LAST SERP AS ENTRANCE FOR THE NEXT SIMULATION STEP
                        snippets_concat = "" ### IN THE FIRST VARIANT WE CONCAT ALL THE SNIPPETS
                        # print("SERP", serp)
                        for entry in serp[3].values():
                            snippets_concat += "Title: \""+entry["Headline"] + "\" Snippet: \"" + entry["Snippet"] +'\"\n' # "\" Snippet: \"" + entry["Snippet"] +'\"\n' #
                        query_gen = second_step_gen(serp[1], serp[2], serp[0], snippets_concat, None)
                        query_gen = query_gen.replace('"', '')
                        session_queries[orig_url].append(query_gen)
                        print(session_queries[orig_url])
                        serp = bing_search(query_gen) ##### !!!!! I NEED TO MODIFY THE FRESHNESS
                        headline = last_serps[orig_url][1] #### WE NEED TO PROPAGATE THE HEADLINE AND THE ORIGINAL TEXT (NONE, PARAGRAPH OR FULL TEXT) TO AVOID ERRORS
                        text = last_serps[orig_url][2]
                        last_serps[orig_url] = [session_queries[orig_url], headline, text, serp] #### UPDATE LAST SERP
                        time.sleep(2) ### DELAY IN CALLS TO BING SEARCH API
                        avg_score = eval_serp(serp)
                        print(avg_score)
                        newline = {"URL":orig_url, "query":query_gen, "SERP":serp, "AVG_SCORE": avg_score, "STEP": i+1}
                        session = pd.concat([session, pd.DataFrame([newline])], ignore_index=True)

                elif second_step_mode=='full_text': #### !!!!! A VECES NO APARECE EL PRIMER-SEGUNDO TEXTO
                    for orig_url, serp in last_serps.items(): # WE USE THE LAST SERP AS ENTRANCE FOR THE NEXT SIMULATION STEP
                        full_text_snippets_concat = "" ### IN THE FIRST VARIANT WE CONCAT ALL THE SNIPPETS
                        for i, entry in enumerate(serp[3].values()):
                            if i==0 or i==1:
                                full_text_snippets_concat +=  "Title: \""+entry["Headline"] + "\" Snippet: \"" + entry["Snippet"] +'\" Full Text: \"'+entry["Full_text"]+'\"\n'
                            else:
                                full_text_snippets_concat += "Title: \""+entry["Headline"] + "\" Snippet: \"" + entry["Snippet"] +'\"\n'
                        query_gen = second_step_gen(serp[1], serp[2], serp[0], None, full_text_snippets_concat)
                        query_gen = query_gen.replace('"', '')
                        print(query_gen)
                        serp = bing_search(query_gen, True) ##### !!!!! I NEED TO MODIFY THE FRESHNESS
                        headline = last_serps[orig_url][1] #### WE NEED TO PROPAGATE THE HEADLINE AND THE ORIGINAL TEXT (NONE, PARAGRAPH OR FULL TEXT) TO AVOID ERRORS
                        text = last_serps[orig_url][2]
                        last_serps[orig_url] = [query_gen, headline, text, serp] #### UPDATE LAST SERP
                        time.sleep(2) ### DELAY IN CALLS TO BING SEARCH API
                        avg_score = eval_serp(serp)
                        newline = {"URL":orig_url, "query":query_gen, "SERP":serp, "AVG_SCORE": avg_score, "STEP": i+1}
                        session = pd.concat([session, pd.DataFrame([newline])], ignore_index=True)

        ###### SALVAR EN UN CSV
        session.to_csv(SIM_DIR+f'/{first_step_mode}_{second_step_mode}/session_{first_step_mode}_{second_step_mode}_steps_{sample}_{count}.csv', sep=',', index=False, header=True)
        print("======SESSION ENDED========")
        count+=1

if __name__=="__main__":
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_DIR = os.path.join(BASE_DIR, "data")
    SIM_DIR = os.path.join(BASE_DIR, "sim_output")
     ## Set the API key and model name
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", OPENAI_API_KEY))
    first_step_mode = sys.argv[1] # other modes 'paragraph', 'full_text'
    second_step_mode = sys.argv[2] # other modes 'full_text'
    corpus = pd.read_csv(DATA_DIR+'/corpus_def.csv')
    simulate(corpus)