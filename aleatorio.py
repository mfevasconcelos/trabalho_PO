import random
import pandas as pd
import os

num_enfermeiros = 13
dias_no_mes = 28
enfermeiros = [f'Enf_{i+1}' for i in range(num_enfermeiros)]
dias = range(1, dias_no_mes + 1)
random.seed(42) 
pedidos_folga = {}

for e in enfermeiros:
    for d in dias:
        pedidos_folga[(e, d)] = 1 if random.random() < 0.5 else 0

s = pd.Series(pedidos_folga)
s.index = pd.MultiIndex.from_tuples(s.index, names=['Enfermeiro', 'Dia'])

df_pivot = s.unstack(level='Dia')

df_pivot.columns = [f'Dia {d}' for d in df_pivot.columns]
df_pivot = df_pivot.reset_index() 

nome_arquivo_csv = 'matriz_pedidos_folga.csv'
df_pivot.to_csv(nome_arquivo_csv, index=False)

print("-" * 50)
print(f"Matriz exportada para o arquivo: {nome_arquivo_csv}")
print(f"arquivo foi salvo: {os.path.abspath(nome_arquivo_csv)}")
print("-" * 50)

print("\n Matriz no Terminal:")
print(df_pivot)