import matplotlib as mpl
import pandas as pd
import matplotlib.pyplot as plt
mpl.use('Agg')
df = pd.read_csv('informacoes.csv')
# eixoX = ['Branca', 'Preta', 'Amarela', 'Parda', 'indigena']
# eixoY = []
eixoX = df['Cor']
# eixoY = df['Total']
eixoY = df['Percentual']
fig, ax = plt.subplots(figsize=(8, 5))
plt.title("Declarações")
plt.bar(eixoX, eixoY)
plt.xticks(rotation=45, ha='right')
plt.savefig('grafico-de-barras.png')
