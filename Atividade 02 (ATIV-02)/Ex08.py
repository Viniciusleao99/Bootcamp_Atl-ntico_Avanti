#Utilizando pandas, como realizar a leitura de um arquivo CSV em um DataFrame e exibir as primeiras linhas?

import pandas 

nome_do_arquivo = 'nome_do_arquivo.csv'

df = pandas.read_csv(nome_do_arquivo)

print(df.head())