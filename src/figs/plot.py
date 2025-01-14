import ast
import os
from urllib.parse import urlparse
import matplotlib.pyplot as plt
import pandas as pd
import sys
import numpy as np
from scipy.stats import mannwhitneyu


'''
This script generates Fig. 4 in the paper for evaluating NewsGuard Scores at different rank positions. 
It also runs stats tests at this different rank positions
'''

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

results_6 = {step: [] for step in range(1,6)}
for f in os.listdir('./sim_output/full_text_full_text/bing-api/'):
  if f.startswith('session_full_text_full_text_steps'):
    df = pd.read_csv('./sim_output/full_text_full_text/bing-api/'+f)
    #df['step'] = (df.index//17) +1
    dd = df.groupby("STEP")["SERP"].apply(list).to_dict()
    for step, values in dd.items():
      results_6[step].extend(values)

newsguard = pd.read_csv('./data/overall_bias.csv', sep=';')
scores = {}

# step = int(sys.argv[1])

for step in range(1,6):
    for i,variant in enumerate([results[step], results_2[step], results_3[step], results_4[step], results_5[step], results_6[step]]):
        if i==0:
            var = "H - TS"
            if not var in scores:
                scores[var] = {i: [] for i in range(1,11)}
        if i==1:
            var = "H 1P - TS"
            if not var in scores:
                scores[var] = {i: [] for i in range(1,11)}
        if i==2:
            var = "FT - TS"
            if not var in scores:
                scores[var] = {i: [] for i in range(1,11)}
        if i==3:
           var = "H - TS 1P TOP2"
           if not var in scores:
                scores[var] = {i: [] for i in range(1,11)}
        if i==4:
           var = "H 1P - TS 1P TOP2"
           if not var in scores:
                scores[var] = {i: [] for i in range(1,11)}
        if i==5:
           var = "FT - TS 1P TOP2"
           if not var in scores:
                scores[var] = {i: [] for i in range(1,11)}
        for serp in variant:
            serp = ast.literal_eval(serp)
            for pos, val in serp.items():
                # print(pos, val['URL'])
                domain = urlparse(val["URL"]).netloc
                domain = domain.replace('www.', '')
                if domain in newsguard["domain"].values:
                    score = newsguard.loc[newsguard["domain"]==domain, "newsguard"].values[0]
                    score = float(score.replace(',', '.'))
                    scores[var][pos].append(score) 
  # print()
  # print()


print(len(scores['H - TS'][1]))
print(len(scores['H 1P - TS'][1]))

print(mannwhitneyu(scores['H - TS'][1], scores['FT - TS'][1]))
print(mannwhitneyu(scores['H - TS'][1], scores['H 1P - TS'][1]))
print(mannwhitneyu(scores['H - TS'][1], scores["H - TS 1P TOP2"][1]))
print(mannwhitneyu(scores['H - TS'][1], scores["H 1P - TS 1P TOP2"][1]))
print()
print()
#########
print(mannwhitneyu(scores['H 1P - TS'][1], scores['FT - TS'][1]))
print(mannwhitneyu(scores['H 1P - TS'][1], scores["H - TS 1P TOP2"][1]))
print(mannwhitneyu(scores['H 1P - TS'][1], scores["H 1P - TS 1P TOP2"][1]))
print()
print()
#########
print(mannwhitneyu(scores['FT - TS'][1], scores["H - TS 1P TOP2"][1]))
print(mannwhitneyu(scores['FT - TS'][1], scores["H 1P - TS 1P TOP2"][1]))
print()
print()
#########
print(mannwhitneyu(scores["H - TS 1P TOP2"][1], scores["H 1P - TS 1P TOP2"][1]))
print()
print()
############
print(mannwhitneyu(scores["FT - TS 1P TOP2"][1], scores['H - TS'][1]))
print(mannwhitneyu(scores["FT - TS 1P TOP2"][1], scores['FT - TS'][1]))
print(mannwhitneyu(scores["FT - TS 1P TOP2"][1], scores['H 1P - TS'][1]))
print(mannwhitneyu(scores["FT - TS 1P TOP2"][1], scores["H - TS 1P TOP2"][1]))
print(mannwhitneyu(scores["FT - TS 1P TOP2"][1], scores["H 1P - TS 1P TOP2"][1]))
print()
print()
#########


for k,val in scores.items():
  scores[k] = {k:np.mean(v) for k,v in val.items()}

plt.figure(figsize=(8,6))


markers = ['o', 's', '^', 'v', 'd', 'x']
m=0
for variant, values in scores.items():
  xs = list(values.keys())
  ys = list(values.values())
  plt.plot(xs, ys, marker=markers[m], label=variant)
  m+=1

plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().spines['bottom'].set_visible(False)
plt.gca().xaxis.set_ticks_position('none')
plt.gca().yaxis.set_ticks_position('none')
plt.legend()
plt.savefig('all-variants.png')
plt.show()