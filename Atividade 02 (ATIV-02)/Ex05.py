"""Crie uma função que receba uma lista de tuplas, cada uma contendo o nome e a idade 
de uma pessoa, e retorne a lista ordenada pelo nome das pessoas em ordem alfabética."""

def ordem_alfabetica(lista_de_pessoas):
    
    n = len(lista_de_pessoas)
    for i in range(n):
        for j in range(0, n-i-1):
            
            if lista_de_pessoas[j][0] > lista_de_pessoas[j+1][0]:
                lista_de_pessoas[j], lista_de_pessoas[j+1] = lista_de_pessoas[j+1], lista_de_pessoas[j]
    return lista_de_pessoas

lista_de_pessoas = [("João", 25), ("Ana", 30), ("Pedro", 20), ("Maria", 35)]

lista_ordenada = ordem_alfabetica(lista_de_pessoas)

print(lista_ordenada)