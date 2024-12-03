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

results_5 = {step: [] for step in range(1,6)}
for f in os.listdir('./sim_output/paragraph_full_text/bing-api/'):
  if f.startswith('session_paragraph_full_text_steps'):
    df = pd.read_csv('./sim_output/paragraph_full_text/bing-api/'+f)
    #df['step'] = (df.index//17) +1
    dd = df.groupby("STEP")["SERP"].apply(list).to_dict()
    for step, values in dd.items():
      results_5[step].extend(values)

newsguard = pd.read_csv('./data/overall_bias.csv', sep=';')
scores = {}

# step = int(sys.argv[1])

for step in range(1,6):
    for i,variant in enumerate([results[step], results_2[step], results_3[step], results_4[step], results_5[step]]):
        if i==0:
            var = "title + snippets"
            if not var in scores:
                scores[var] = {step: [] for step in range(1,11)}
        if i==1:
            var = "paragraph + snippets"
            if not var in scores:
                scores[var] = {step: [] for step in range(1,11)}
        if i==2:
            var = "full text + snippets"
            if not var in scores:
                scores[var] = {step: [] for step in range(1,11)}
        if i==3:
           var = "title + first two entries"
           if not var in scores:
                scores[var] = {step: [] for step in range(1,11)}
        if i==4:
           var = "paragraph + first two entries"
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

print(scores.keys())
title, paragraph, full, title_full, par_full = [],[],[],[], []
for k,v in scores.items():
  if k=="title + snippets":
    title.extend([val for val in v.values()])
  elif k=="paragraph + snippets":
    paragraph.extend([val for val in v.values()])
  elif k=="full text + snippets":
    full.extend([val for val in v.values()])
  elif k=="title + first two entries":
    title_full.extend([val for val in v.values()])
  elif k=="paragraph + first two entries":
    par_full.extend([val for val in v.values()])


print(len(title), len(paragraph), len(full), len(title_full), len(par_full))

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
res = wilcoxon(par_full, paragraph, alternative='greater')
print(res)
res = wilcoxon(par_full, paragraph, alternative='greater')
print(res)
res = wilcoxon(par_full, full, alternative='greater')
print(res)
res = wilcoxon(par_full, title, alternative='greater')
print(res)
res = wilcoxon(par_full, title_full, alternative='greater')
print(res)