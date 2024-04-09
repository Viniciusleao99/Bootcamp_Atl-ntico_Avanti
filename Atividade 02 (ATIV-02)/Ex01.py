#Escreva uma função que receba uma lista de números e retorne outra lista com os números ímpares.

def numeros_impares(lista):
    return [numero for numero in lista if numero % 2 != 0]

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_impares_lista = numeros_impares(lista_numeros)
print("os numeros impares da lista sao: {}".format(numeros_impares_lista))