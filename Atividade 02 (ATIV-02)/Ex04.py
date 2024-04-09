#Dada uma lista de números inteiros, escreva uma função para encontrar o segundo maior valor na lista.

def segundo_maior(lista):
    lista_ordenada = sorted(lista, reverse=True)
    
    if len(lista_ordenada) >= 2:

        return lista_ordenada[1]
    else:
        return "A lista possui menos de dois elementos."

numeros = [10, 5, 20, 15, 25]
segundo_maior_valor = segundo_maior(numeros)
print("O segundo maior valor na lista é:", segundo_maior_valor)