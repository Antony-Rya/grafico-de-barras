import matplotlib as mpl
import pandas as pd
mpl.use('Agg')
import matplotlib.pyplot as plt
df = pd.read_csv('informacoes.csv')
eixoX = df['Cor']
eixoY = df["Percentual"]
fig, ax = plt.subplots(figsize=(8, 5))
plt.title("Declarações")
plt.bar(eixoX, eixoY)
plt.xticks(rotation=45, ha='right')
plt.savefig('grafico-de-barras.png')
