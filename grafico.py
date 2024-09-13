import matplotlib as mpl
import pandas as pd
mpl.use('Agg')
import matplotlib.pyplot as plt
df = pd.read_csv('informacoes.csv')
eixoX = df['Disciplina']
eixoY = df['Nota']

plt.title("Notas do aluno")
plt.bar(eixoX, eixoY)
plt.savefig('imagem.png')
