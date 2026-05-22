def calcular_media(numeros):
    resultado = sum(numeros)/len(numeros)
    
    return resultado

lista_numeros = [1, 5, 10, 12, 15]


print (calcular_media(lista_numeros))



def palavras_longas(palavras):
    maior_palavra = max(palavras, key=len)


    return maior_palavra
    


lista_palavras = ['Oi', 'Olá', 'Aoba']

print(palavras_longas(lista_palavras))