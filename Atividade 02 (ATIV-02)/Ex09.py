#Utilizando pandas, como selecionar uma coluna específica e filtrar linhas em um “DataFrame” com base em uma condição?
#data_frame é o nome do DataFrame do exemplo e queromos selecionar as linhas com base na condição de ano maior que 2001
import pandas

coluna_idade = data_frame['ano']

linhas_filtradas = data_frame[data_frame['ano'] > 2001 ]

print(linhas_filtradas)
