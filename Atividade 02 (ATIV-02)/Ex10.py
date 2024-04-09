#Utilizando pandas, como lidar com valores ausentes (NaN) em um DataFrame?

"""Para lidar com valores ausentes em um DataFrame com Pandas, existem várias técnicas, 
como identificar, remover ou preencher esses valores ausentes. 
Segue alguns exemplos práticos:"""

#Identificar valores ausentes:

print(data_frame.isnull().sum())

print(data_frame['nome_da_coluna'].isnull().sum())

#Remover linhas ou colunas com valores ausentes:

data_frame_remover= data_frame.dropna()

data_frame_remover_linha = data_frame.dropna(axis=1)

#Preencher valores ausentes com um valor específico:

data_frame_preenchido = data_frame.fillna(0)

media_idade = data_frame['idade'].mean()
data_frame_preenchido_media = data_frame.fillna(media_idade)

#Interpolar valores ausentes:

data_frame_interpolar = data_frame.interporar()
