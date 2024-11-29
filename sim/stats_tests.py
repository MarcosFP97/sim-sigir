import os
import numpy as np
import pandas as pd
from scipy.stats import mannwhitneyu

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
#print(f'{results_3}')


##### STATS TESTS
for i in range(1,6):
    scores_estrategia_1 = [x for x in results[i] if not np.isnan(x)]
    scores_estrategia_2 = [x for x in results_2[i] if not np.isnan(x)]
    scores_estrategia_3 = [x for x in results_3[i] if not np.isnan(x)]
    stat1, p_value1 = mannwhitneyu(scores_estrategia_1, scores_estrategia_2)
    print(np.median(scores_estrategia_1), np.median(scores_estrategia_2))
    print(f"U (estrategia 1 vs 2): {stat1}, p-value: {p_value1}")
    print("==========================================================")
    print(np.median(scores_estrategia_2), np.median(scores_estrategia_3))
    stat1, p_value1 = mannwhitneyu(scores_estrategia_2, scores_estrategia_3)
    print(f"U (estrategia 2 vs 3): {stat1}, p-value: {p_value1}")
    print("============================================================")
    print()
    print()

#### MEDIAS
for i in range(1,6):
  scores_estrategia_1 = [x for x in results[i] if not np.isnan(x)]
  scores_estrategia_2 = [x for x in results_2[i] if not np.isnan(x)]
  scores_estrategia_3 = [x for x in results_3[i] if not np.isnan(x)]
  # print(np.mean(scores_estrategia_1))
  # print(np.mean(scores_estrategia_2))
  print(np.mean(scores_estrategia_3))

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



