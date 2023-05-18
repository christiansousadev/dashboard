import pandas as pd

# Carregar o arquivo do Excel
caminho_arquivo = 'dash.xlsx'
dados = pd.read_excel(caminho_arquivo)

# Exibir os dados do arquivo
print(dados)

# Calcular o total de vendas
total_vendas = dados['Faturamento'].sum()
print('Faturamento trimestre:', total_vendas)

# Calcular a média de vendas
media_vendas = dados['Faturamento'].mean()
print('Média das vendas:', media_vendas)

# Calcular o valor máximo e mínimo das vendas
valor_maximo = dados['Faturamento'].max()
valor_minimo = dados['Faturamento'].min()
print('Valor máximo de vendas é:', valor_maximo)
print('Valor mínimo de vendas é:', valor_minimo)

# Cálculo do somatório das equipes
vendas_por_equipe = dados['Equipe'].value_counts()
print('Vendas por equipe:')
print(vendas_por_equipe)
