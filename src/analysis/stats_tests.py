import os
import numpy as np
import pandas as pd
from scipy.stats import mannwhitneyu

h_ts = []
for f in os.listdir('./sim_output/title_snippet/bing-api/'):
  if f.startswith('session_title_snippet_steps'):
    df = pd.read_csv('./sim_output/title_snippet/bing-api/'+f)
    # df = df[df["STEP"]==1]
    h_ts.extend(df["AVG_SCORE"].values)

h_1p_ts = []
for f in os.listdir('./sim_output/paragraph_snippet/bing-api/'):
  if f.startswith('session_paragraph_snippet_steps'):
    df = pd.read_csv('./sim_output/paragraph_snippet/bing-api/'+f)
    # df = df[df["STEP"]==1]
    h_1p_ts.extend(df["AVG_SCORE"].values)

ft_ts = []
for f in os.listdir('./sim_output/full_text_snippet/bing-api/'):
  if f.startswith('session_full_text_snippet_steps'):
    df = pd.read_csv('./sim_output/full_text_snippet/bing-api/'+f)
    # df = df[df["STEP"]==1]
    ft_ts.extend(df["AVG_SCORE"].values)

h_ts_1p_top2 = []
for f in os.listdir('./sim_output/title_full_text/bing-api/'):
  if f.startswith('session_title_full_text_steps'):
    df = pd.read_csv('./sim_output/title_full_text/bing-api/'+f)
    # df = df[df["STEP"]==1]
    # print(df)
    h_ts_1p_top2.extend(df["AVG_SCORE"].values)

h_1p_ts_1p_top2 = []
for f in os.listdir('./sim_output/paragraph_full_text/bing-api/'):
  if f.startswith('session_paragraph_full_text_steps'):
    df = pd.read_csv('./sim_output/paragraph_full_text/bing-api/'+f)
    # df = df[df["STEP"]==1]
    # print(df)
    h_1p_ts_1p_top2.extend(df["AVG_SCORE"].values)

ft_ts_1p_top2 = []
for f in os.listdir('./sim_output/full_text_full_text/bing-api/'):
  if f.startswith('session_full_text_full_text_steps'):
    df = pd.read_csv('./sim_output/full_text_full_text/bing-api/'+f)
    # df = df[df["STEP"]==1]
    ft_ts_1p_top2.extend(df["AVG_SCORE"].values)

h_ts = [x for x in h_ts if str(x) != 'nan']
h_1p_ts = [x for x in h_1p_ts if str(x) != 'nan']
ft_ts = [x for x in ft_ts if str(x) != 'nan']
h_ts_1p_top2 = [x for x in h_ts_1p_top2 if str(x) != 'nan']
h_1p_ts_1p_top2 = [x for x in h_1p_ts_1p_top2 if str(x) != 'nan']
ft_ts_1p_top2 = [x for x in ft_ts_1p_top2 if str(x) != 'nan']
print(f'{len(h_ts)}')
print(f'{len(h_1p_ts)}')
print(f'{len(ft_ts)}')
print(f'{len(ft_ts_1p_top2)}')
print(f'{len(h_ts_1p_top2)}')
print(f'{len(h_1p_ts_1p_top2)}')

print(mannwhitneyu(h_ts, ft_ts))
print(mannwhitneyu(h_ts, h_1p_ts))
print(np.mean(h_ts), np.std(h_ts))
print(np.mean(h_ts_1p_top2), np.std(h_ts_1p_top2))
print("Aquí", mannwhitneyu(h_ts, h_ts_1p_top2))
print(np.mean(h_ts))
print(np.mean(h_1p_ts_1p_top2))
print(mannwhitneyu(h_ts, h_1p_ts_1p_top2))
print()
print()
#########
print(mannwhitneyu(h_1p_ts, ft_ts))
print(mannwhitneyu(h_1p_ts, h_ts_1p_top2))
print(np.mean(h_1p_ts), np.std(h_1p_ts))
print(np.mean(h_1p_ts_1p_top2), np.std(h_1p_ts_1p_top2))
print("Aquí 2", mannwhitneyu(h_1p_ts, h_1p_ts_1p_top2))
print()
print()
#########
print(mannwhitneyu(ft_ts, h_ts_1p_top2))
print(mannwhitneyu(ft_ts, h_1p_ts_1p_top2))
print()
print()
#########
print(np.mean(h_ts_1p_top2))
print(np.mean(h_1p_ts_1p_top2))
print(mannwhitneyu(h_ts_1p_top2, h_1p_ts_1p_top2))
print()
print()
###########
print(np.mean(ft_ts_1p_top2))
print(np.mean(h_ts))
print(mannwhitneyu(ft_ts_1p_top2, h_ts))
print(np.mean(ft_ts), np.std(ft_ts))
print(np.mean(ft_ts_1p_top2), np.std(ft_ts_1p_top2))
print("Aquí 3", mannwhitneyu(ft_ts_1p_top2, ft_ts))
print(np.mean(h_1p_ts))
print(mannwhitneyu(ft_ts_1p_top2, h_1p_ts))
print(np.mean(h_ts_1p_top2))
print(mannwhitneyu(ft_ts_1p_top2, h_ts_1p_top2))
print(np.mean(h_1p_ts_1p_top2))
print(mannwhitneyu(ft_ts_1p_top2, h_1p_ts_1p_top2))
print()
print()
#########

h = h_ts + h_ts_1p_top2
h1 = h_1p_ts + h_1p_ts_1p_top2
ft = ft_ts + ft_ts_1p_top2
print(np.std(h))
print(len(h))
print(np.std(h1))
print(len(h1))
print(np.std(ft))
print(len(ft))
print(mannwhitneyu(h, h1))
print(mannwhitneyu(h1, ft))
print(mannwhitneyu(ft, h))