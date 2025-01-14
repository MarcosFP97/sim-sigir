import os
import pandas as pd

results = {step: [] for step in range(1,6)}
for f in os.listdir('./sim_output/full_text_full_text/bing-api/'):
  if f.startswith('session_full_text_full_text_steps'):
    df = pd.read_csv('./sim_output/full_text_full_text/bing-api/'+f)
    #df['step'] = (df.index//17) +1
    print()
    print()
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
# Configurar las etiquetas en el eje x según el orden
plt.xticks(range(1, len(claves_ordenadas) + 1), claves_ordenadas)

# Añadir título y etiquetas a los ejes
# plt.full_text("Boxplots con claves ordenadas")
plt.xlabel("Query position in session")
# plt.ylim(50, 105)
plt.savefig('full_text-full_text.png')
plt.show()
import numpy as np
for i in valores_ordenados:
  print(np.median(i))


# plt.ylabel("Valores")

# Mostrar el gráfico
