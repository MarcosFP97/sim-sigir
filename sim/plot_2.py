import ast
import os
from urllib.parse import urlparse
import matplotlib.pyplot as plt
import pandas as pd
import sys
import numpy as np

results = {step: [] for step in range(1,6)}
for f in os.listdir('./sim_output/title_snippet/bing-api/'):
  if f.startswith('session_title_snippet_steps'):
    df = pd.read_csv('./sim_output/title_snippet/bing-api/'+f)
    dd = df.groupby("STEP")["SERP"].apply(list).to_dict()
    for step, values in dd.items():
      results[step].extend(values)
#print(f'{results}')

results_2 = {step: [] for step in range(1,6)}
for f in os.listdir('./sim_output/paragraph_snippet/bing-api/'):
  if f.startswith('session_paragraph_snippet_steps'):
    df = pd.read_csv('./sim_output/paragraph_snippet/bing-api/'+f)
    dd = df.groupby("STEP")["SERP"].apply(list).to_dict()
    for step, values in dd.items():
      results_2[step].extend(values)
#print(f'{results_2}')

results_3 = {step: [] for step in range(1,6)}
for f in os.listdir('./sim_output/full_text_snippet/bing-api/'):
  if f.startswith('session_full_text_snippet_steps'):
    df = pd.read_csv('./sim_output/full_text_snippet/bing-api/'+f)
    dd = df.groupby("STEP")["SERP"].apply(list).to_dict()
    for step, values in dd.items():
      results_3[step].extend(values)

results_4 = {step: [] for step in range(1,6)}
for f in os.listdir('./sim_output/title_full_text/bing-api/'):
  if f.startswith('session_title_full_text_steps'):
    df = pd.read_csv('./sim_output/title_full_text/bing-api/'+f)
    df['step'] = (df.index//17) +1
    dd = df.groupby("step")["SERP"].apply(list).to_dict()
    for step, values in dd.items():
      results_4[step].extend(values)

newsguard = pd.read_csv('./data/overall_bias.csv', sep=';')
scores = {}

# step = int(sys.argv[1])

for step in range(1,6):
    for i,variant in enumerate([results[step], results_2[step], results_3[step], results_4[step]]):
        if i==0:
            var = "title"
            if not var in scores:
                scores[var] = {step: [] for step in range(1,11)}
        if i==1:
            var = "paragraph"
            if not var in scores:
                scores[var] = {step: [] for step in range(1,11)}
        if i==2:
            var = "full"
            if not var in scores:
                scores[var] = {step: [] for step in range(1,11)}
        if i==3:
           var = "title+full"
           if not var in scores:
                scores[var] = {step: [] for step in range(1,11)}
        for serp in variant:
            serp = ast.literal_eval(serp)
            for pos, val in serp.items():
                #print(pos, val['URL'])
                domain = urlparse(val["URL"]).netloc
                domain = domain.replace('www.', '')
                if domain in newsguard["domain"].values:
                    score = newsguard.loc[newsguard["domain"]==domain, "newsguard"].values[0]
                    score = float(score.replace(',', '.'))
                    scores[var][pos].append(score) 
  # print()
  # print()


print(len(scores["title"][10]))

for k,val in scores.items():
  scores[k] = {k:np.mean(v) for k,v in val.items()}

plt.figure(figsize=(8,6))

for variant, values in scores.items():
  xs = list(values.keys())
  ys = list(values.values())
  plt.plot(xs, ys, marker='o', label=variant)

plt.legend()
plt.savefig('all-variants.png')
plt.show()

print(scores)
title, paragraph, full, title_full = [],[],[],[]
for k,v in scores.items():
  if k=="title":
    title.extend([val for val in v.values()])
  elif k=="paragraph":
    paragraph.extend([val for val in v.values()])
  elif k=="full":
    full.extend([val for val in v.values()])
  elif k=="title+full":
    title_full.extend([val for val in v.values()])


from scipy.stats import wilcoxon
res = wilcoxon(paragraph, title, alternative='greater')
print(res)
res = wilcoxon(paragraph, full, alternative='greater')
print(res)
res = wilcoxon(full, title, alternative='greater')
print(res)
res = wilcoxon(title_full, title, alternative='greater')
print(res)
res = wilcoxon(title_full, full, alternative='greater')
print(res)
res = wilcoxon(title_full, paragraph, alternative='greater')
print(res)