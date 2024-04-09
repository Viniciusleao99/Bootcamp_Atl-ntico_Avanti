#Escreva uma função que receba duas listas e retorne outra lista com os elementos que estão presentes em apenas uma das listas

def elementos_unicos(lista1, lista2):
    elementos_unicos_lista = []
    for elemento in lista1:
        if elemento not in lista2:
            elementos_unicos_lista.append(elemento)
    for elemento in lista2:
        if elemento not in lista1:
            elementos_unicos_lista.append(elemento)
    return elementos_unicos_lista

# Exemplo de uso:
lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]
resultado = elementos_unicos(lista1, lista2)
print("A lista com elementos que não se repetem nas listas é {}:".format(resultado))
