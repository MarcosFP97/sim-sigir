import os
import numpy as np
import pandas as pd
from scipy.stats import mannwhitneyu

results = {step: [] for step in range(1,6)}
for f in os.listdir('./sim_output/title_snippet/bing-api/'):
  if f.startswith('session_title_snippet_steps'):
    df = pd.read_csv('./sim_output/title_snippet/bing-api/'+f)
    dd = df.groupby("STEP")["AVG_SCORE"].apply(list).to_dict()
    for step, values in dd.items():
      results[step].extend(values)
print(f'{results}')

results_2 = {step: [] for step in range(1,6)}
for f in os.listdir('./sim_output/paragraph_snippet/bing-api/'):
  if f.startswith('session_paragraph_snippet_steps'):
    df = pd.read_csv('./sim_output/paragraph_snippet/bing-api/'+f)
    dd = df.groupby("STEP")["AVG_SCORE"].apply(list).to_dict()
    for step, values in dd.items():
      results_2[step].extend(values)
print(f'{results_2}')

for i in range(1,6):
    scores_estrategia_1 = [x for x in results[i] if not np.isnan(x)]
    scores_estrategia_2 = [x for x in results_2[i] if not np.isnan(x)]
    stat1, p_value1 = mannwhitneyu(scores_estrategia_1, scores_estrategia_2)
    print(f"U (estrategia 1 vs 2): {stat1}, p-value: {p_value1}")
