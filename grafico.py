import matplotlib as mpl
import pandas as pd
mpl.use('Agg')
import matplotlib.pyplot as plt
df = pd.read_csv('informacoes.csv')
eixoX = df['Nome do Aluno']
eixoY = df['Média']
fig, ax = plt.subplots(figsize=(8, 10))
plt.title("Notas do aluno")
plt.bar(eixoX, eixoY)
plt.xticks(rotation=45, ha='right')
plt.savefig('imagem.png')
