import os
import pandas as pd

results = {step: [] for step in range(1,9)}
for f in os.listdir('./sim_output/title_snippet'):
  if f.startswith('session_title_snippet_steps'):
    df = pd.read_csv('./sim_output/title_snippet/'+f)
    dd = df.groupby("STEP")["AVG_SCORE"].apply(list).to_dict()
    for step, values in dd.items():
      results[step].extend(values)
print(f'{results}')
import matplotlib.pyplot as plt
import numpy as np
# Crear el boxplot
mi_diccionario_sin_nan = {k: [v for v in valores if not np.isnan(v)] for k, valores in results.items()}

# Crear el boxplot
claves_ordenadas = sorted(mi_diccionario_sin_nan.keys())

# Reorganizar los valores según el orden de las claves
valores_ordenados = [mi_diccionario_sin_nan[clave] for clave in claves_ordenadas]

# Crear el boxplot
plt.boxplot(valores_ordenados)
plt.savefig('title-snippet.png')

import numpy as np
for i in valores_ordenados:
  print(np.median(i))

# Configurar las etiquetas en el eje x según el orden
plt.xticks(range(1, len(claves_ordenadas) + 1), claves_ordenadas)

# Añadir título y etiquetas a los ejes
# plt.title("Boxplots con claves ordenadas")
plt.xlabel("Query position in session")
# plt.ylabel("Valores")

# Mostrar el gráfico
plt.show()